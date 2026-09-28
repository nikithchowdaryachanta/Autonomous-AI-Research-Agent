import streamlit as st
from researchpilot.agent import ResearchAgent
from researchpilot.config import Settings
from researchpilot.reporting import pdf_report

st.set_page_config(
    page_title="ResearchPilot",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 ResearchPilot")
st.caption("Autonomous Research Agent — Assessment Option 1")

with st.sidebar:
    st.header("Configuration")

    settings = Settings()

    max_sources = st.slider(
        "Maximum sources",
        min_value=3,
        max_value=12,
        value=6,
    )

    use_memory = st.checkbox(
        "Use previous-search memory",
        value=True,
    )

    st.divider()

    st.write(
        f"LLM: Google Gemini / `{settings.gemini_model}`"
    )

    st.write(
        "Gemini: " +
        ("configured" if settings.gemini_api_key else "not configured")
    )

    st.write(
        "Tavily: " +
        ("configured" if settings.tavily_api_key else "not configured")
    )

query = st.text_area(
    "Research topic / question",
    placeholder=(
        "Example: What are the main applications and "
        "limitations of retrieval augmented generation?"
    ),
    height=110,
)

if st.button(
    "Run Autonomous Research",
    type="primary",
    disabled=not query.strip(),
):
    try:
        with st.spinner(
            "Planning, researching, filtering and synthesizing..."
        ):
            result = ResearchAgent(settings).run(
                query.strip(),
                max_sources=max_sources,
                use_memory=use_memory,
            )

        st.session_state["result"] = result

    except Exception as error:
        st.error(str(error))

result = st.session_state.get("result")

if result:
    metrics = result["metrics"]

    columns = st.columns(4)
    columns[0].metric(
        "Sources Gathered",
        metrics["sources_gathered"],
    )
    columns[1].metric(
        "Sources Retained",
        metrics["sources_retained"],
    )
    columns[2].metric(
        "Duplicates Removed",
        metrics["duplicates_removed"],
    )
    columns[3].metric(
        "Latency",
        f'{metrics["latency_seconds"]:.1f}s',
    )

    tabs = st.tabs(
        [
            "Research Report",
            "Sources",
            "Agent Trace",
            "Monitoring",
        ]
    )

    with tabs[0]:
        st.markdown(result["report"]["markdown"])

        st.download_button(
            "Download Markdown",
            result["report"]["markdown"].encode(),
            file_name="research_report.md",
            mime="text/markdown",
        )

        st.download_button(
            "Download PDF",
            pdf_report(
                result["report"],
                result["sources"],
            ),
            file_name="research_report.pdf",
            mime="application/pdf",
        )

    with tabs[1]:
        for source in result["sources"]:
            with st.expander(
                f'[{source["id"]}] {source["title"]}'
            ):
                st.write(source.get("snippet", ""))
                st.write(f'Source: {source["url"]}')
                st.write(
                    f'Relevance: '
                    f'{source.get("relevance_score", 0):.2f}'
                )

    with tabs[2]:
        for event in result["trace"]:
            st.json(event)

    with tabs[3]:
        st.json(metrics)

        counts = {}
        for source in result["sources"]:
            source_type = source["source_type"]
            counts[source_type] = counts.get(source_type, 0) + 1

        st.subheader("Retrieved Source Types")
        st.bar_chart(counts)
