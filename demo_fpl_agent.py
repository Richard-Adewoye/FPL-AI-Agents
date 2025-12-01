# demo_fpl_agent.py

from sub_agents.root_agent import root_agent
from sub_agents.tools import analyze_team_stats

if __name__ == "__main__":
    try:
        # Step 1: Prepare sample data directory
        sample_data_dir = "data/sample_team_stats"
        stats_context = analyze_team_stats(sample_data_dir)

        # Step 2: Run root agent in demo mode
        # We simulate feedback automatically and skip interactive inputs
        demo_result = root_agent.run_demo(
            initial_state={"codebase_context": stats_context["codebase_context"]}
        )

        # Step 3: Print key outputs
        print("=== Demo FPL Agent Output ===")
        if "team_strategy" in demo_result:
            print(demo_result["team_strategy"])
        if "team_report" in demo_result:
            print(demo_result["team_report"])

    except Exception as e:
        print("Demo failed due to:", e)
        print("Refer to README for full workflow instructions.")
