"""Sales data analyzer module for processing pipeline data."""

import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path


def ensure_output_dir():
    """Ensure output directory exists"""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def plot_sales_by_category(df):
    """Plot sales by category"""
    output_dir = ensure_output_dir()
    sales_by_category = df.groupby("Category")["Sales"].sum()

    plt.figure(figsize=(10, 6))
    sales_by_category.plot(kind="bar")
    plt.title("Total Sales by Product Category")
    plt.ylabel("Total Sales ($)")
    plt.xlabel("Category")
    plt.tight_layout()

    output_path = output_dir / "sales_by_category.png"
    plt.savefig(output_path)
    plt.close()
    print(f"Saved sales by category plot to {output_path}")


def plot_monthly_sales_trend(df):
    """Plot monthly sales trend"""
    output_dir = ensure_output_dir()
    df["Order Month"] = pd.to_datetime(df["Order Date"]).dt.to_period("M")
    monthly_sales = df.groupby("Order Month")["Sales"].sum()

    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.ylabel("Total Sales ($)")
    plt.xlabel("Month")
    plt.grid(True)
    plt.tight_layout()

    output_path = output_dir / "monthly_sales_trend.png"
    plt.savefig(output_path)
    plt.close()
    print(f"Saved monthly sales trend plot to {output_path}")
