#!/usr/bin/env python3
"""
Outrank AI SEO Content & TCO Cost Calculator
Models monthly content production expenditure vs Surfer SEO, Frase, and freelance writers.
"""

import sys

def calculate_outrank_tco(articles_per_month: int, plan: str = "growth"):
    plans = {
        "starter": {"monthly": 49.0, "articles": 10, "overage": 5.0},
        "growth": {"monthly": 99.0, "articles": 30, "overage": 3.5},
        "pro": {"monthly": 199.0, "articles": 100, "overage": 2.0}
    }
    
    cfg = plans.get(plan, plans["growth"])
    base_cost = cfg["monthly"]
    extra_articles = max(0, articles_per_month - cfg["articles"])
    outrank_cost = base_cost + (extra_articles * cfg["overage"])
    
    freelance_cost = articles_per_month * 120.0
    surfer_cost = 89.0 + (articles_per_month * 19.0)
    
    return {
        "articles_per_month": articles_per_month,
        "selected_plan": plan,
        "outrank_total_usd": round(outrank_cost, 2),
        "surfer_total_usd": round(surfer_cost, 2),
        "freelance_total_usd": round(freelance_cost, 2),
        "savings_vs_surfer": round(surfer_cost - outrank_cost, 2),
        "savings_vs_freelance": round(freelance_cost - outrank_cost, 2)
    }

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    p = sys.argv[2] if len(sys.argv) > 2 else "growth"
    res = calculate_outrank_tco(count, p)
    print(f"=== Outrank TCO Calculation for {res['articles_per_month']} Articles/Mo ({res['selected_plan']} Plan) ===")
    print(f"Outrank Total: ${res['outrank_total_usd']}")
    print(f"Surfer SEO Equivalent: ${res['surfer_total_usd']} (Save ${res['savings_vs_surfer']})")
    print(f"Freelance Copywriters: ${res['freelance_total_usd']} (Save ${res['savings_vs_freelance']})")
