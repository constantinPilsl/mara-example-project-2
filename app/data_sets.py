import mara_data_explorer.config
import mara_data_explorer.data_set
from mara_app.monkey_patch import patch


@patch(mara_data_explorer.config.data_sets)
def _data_sets():
    return [
        mara_data_explorer.data_set.DataSet(
            id='python-project-activity', name='Python project activities',
            database_alias='dwh', database_schema='pp_dim', database_table='python_project_activity_data_set',
            default_column_names=['Date', 'Project',
                                  '# Downloads', '# Forks', '# Commits', '# Closed pull requests'],
            use_attributes_table=True),

        mara_data_explorer.data_set.DataSet(
            id='github-repo-activity', name='Github repo activities',
            database_alias='dwh', database_schema='gh_dim', database_table='repo_activity_data_set',
            default_column_names=['Date', 'User', 'Repo',
                                  '# Forks', '# Commits', '# Closed pull requests'],
            use_attributes_table=True),

        mara_data_explorer.data_set.DataSet(
            id='pypi-download-counts', name='PyPI download counts',
            database_alias='dwh', database_schema='pypi_dim', database_table='download_counts_data_set',
            default_column_names=['Download date', 'Project', 'Project version',
                                  'Installer', 'Python version', '# Downloads'],
            use_attributes_table=True),

    ]

# adapt to the favorite chart color of your company
patch(mara_data_explorer.config.charts_color)(lambda: '#008000')
