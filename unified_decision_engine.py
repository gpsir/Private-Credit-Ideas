
def unified_decision_engine(modules_output: dict):
    all_flags = []
    red_flags = 0
    yellow_flags = 0

    for module, output in modules_output.items():
        for flag in output.get('flags', []):
            all_flags.append(f"[{module.upper()}] {flag}")
            if "❌" in flag or "⚠️" in flag:
                red_flags += 1
            elif "🟡" in flag:
                yellow_flags += 1

    if modules_output['lending_risk']['decision'] == "REJECT":
        final_decision = "REJECT"
    elif modules_output['cashflow']['sustainability'] == "At Risk":
        final_decision = "REJECT"
    elif red_flags >= 5:
        final_decision = "REJECT"
    elif red_flags >= 3 or yellow_flags >= 4:
        final_decision = "CONDITIONAL"
    else:
        final_decision = "APPROVE"

    return {
        "final_decision": final_decision,
        "total_flags": len(all_flags),
        "red_flags": red_flags,
        "yellow_flags": yellow_flags,
        "flag_summary": all_flags
    }
