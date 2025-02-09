import pytest
from click.testing import CliRunner
from stack.cli.commands import cli, make_app

def test_cli_exists():
    """Test that the CLI command group exists"""
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'make-app' in result.output

def test_make_app_command(mocker):
    """Test the make-app command with mocked questionary responses"""
    # Mock all questionary prompts
    mocker.patch('questionary.select', side_effect=[
        mocker.Mock(ask=lambda: "Django - Full-featured web framework"),
        mocker.Mock(ask=lambda: "React - Popular UI library"),
        mocker.Mock(ask=lambda: "PostgreSQL"),
    ])
    
    mocker.patch('questionary.checkbox', return_value=mocker.Mock(
        ask=lambda: ["Docker setup", "API documentation"]
    ))
    
    mocker.patch('questionary.text', return_value=mocker.Mock(
        ask=lambda: "test-project"
    ))
    
    mocker.patch('questionary.confirm', return_value=mocker.Mock(
        ask=lambda: True
    ))

    runner = CliRunner()
    result = runner.invoke(make_app)
    
    assert result.exit_code == 0
    assert 'Setting up your project' in result.output



def test_create_fast_api_project():
    """Test the make-app command with mocked questionary responses"""
