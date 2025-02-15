import logging
from atlassian import Bitbucket

# Configure logging to show DEBUG messages (including the curl command debug output)
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s: %(message)s"
)


def demo_post_insights_report():
    # Replace these demo values with your actual Bitbucket instance details.
    url = "http://localhost:7990"  # Your Bitbucket server URL
    username = "admin"
    password = "admin"
    project_key = "PROJ"
    repository_slug = "repo"
    commit_id = "123456789abcdef"  # Dummy commit ID
    report_key = "demo-report"
    report_title = "Demo Insights Report"

    # Report parameters: one string field and one number field.
    report_params = {
        "details": "This is an example report",
        "result": "FAIL",
        "reporter": "Anonymous",
        "link": "http://some-url.org",
        "logo-url": "http://my-logo.org",
        "data": [{"title": "Example coverage", "type": "PERCENTAGE", "value": 85}],
    }

    # Initialize the Bitbucket API client.
    bb = Bitbucket(
        url=url,
        username=username,
        password=password,
    )

    # Create a code insights report.
    logging.info("Creating code insights report...")
    if False:
        report = bb.create_code_insights_report(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            report_key=report_key,
            report_title=report_title,
            **report_params,
        )
        print("Created report:", report)

    # Prepare an annotation.
    annotations = [
        {
            "path": "some/path/to/file",
            "line": 32,
            "message": "Roses are red, Violets are blue, Unexpected { on line 32",
            "severity": "MEDIUM",
        }
    ]

    # Add the annotation(s) to the report.
    logging.info("Adding annotations to the report...")
    added = bb.add_code_insights_annotations_to_report(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        report_key=report_key,
        annotations=annotations,
    )
    print("Added annotations:", added)


if __name__ == "__main__":
    demo_post_insights_report()
