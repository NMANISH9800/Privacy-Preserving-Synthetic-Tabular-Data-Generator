# sdv_cli.py — minimal CPU-friendly CLI for single-table CSVs (or a folder of CSVs)
import argparse
from pathlib import Path
import pandas as pd

from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer

try:
    from sdv.single_table import CTGANSynthesizer
    HAS_CTGAN = True
except Exception:
    HAS_CTGAN = False

def synth_one_csv(csv_path: Path, out_dir: Path, rows: int, synth: str, epochs: int, batch_size: int):
    df = pd.read_csv(csv_path, low_memory=False)
    meta = SingleTableMetadata()
    meta.detect_from_dataframe(df)

    if synth.lower() == "ctgan" and HAS_CTGAN:
        model = CTGANSynthesizer(meta, epochs=epochs, batch_size=batch_size)
    else:
        model = GaussianCopulaSynthesizer(meta)  # fast on CPU

    print(f"[fit] {csv_path.name} (rows={len(df)}) using {model.__class__.__name__}")
    model.fit(df)

    n = rows if rows > 0 else max(len(df), 1000)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{csv_path.stem}_synthetic.csv"
    model.sample(n).to_csv(out_file, index=False)
    print(f"[ok] wrote {out_file.resolve()}")

def main():
    ap = argparse.ArgumentParser(description="Generate synthetic data from CSV(s) with SDV.")
    ap.add_argument("--input", required=True, help="Path to a CSV file or folder containing CSVs")
    ap.add_argument("--output", default="synthetic_out", help="Output folder")
    ap.add_argument("--rows", type=int, default=-1, help="Rows to generate per table (-1 means ~size of real)")
    ap.add_argument("--synth", choices=["gaussian", "ctgan"], default="gaussian", help="Model (gaussian=fast CPU)")
    ap.add_argument("--epochs", type=int, default=50, help="CTGAN epochs (if --synth ctgan)")
    ap.add_argument("--batch_size", type=int, default=256, help="CTGAN batch size (if --synth ctgan)")
    args = ap.parse_args()

    inp = Path(args.input)
    out = Path(args.output)

    if inp.is_file():
        synth_one_csv(inp, out, args.rows, args.synth, args.epochs, args.batch_size)
    else:
        csvs = sorted(inp.glob("*.csv"))
        if not csvs:
            raise SystemExit(f"No CSV files found in {inp}")
        for csv_path in csvs:
            synth_one_csv(csv_path, out, args.rows, args.synth, args.epochs, args.batch_size)

if __name__ == "__main__":
    main()
