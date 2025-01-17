from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators,IntegerField,DecimalField,DateField
from wtforms.validators import DataRequired, Length, NumberRange

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
class PlayerAttributesForm(FlaskForm):
    player_code = StringField('Player Code', validators=[DataRequired(), Length(min=1, max=50)])
    sub_position = StringField('Sub Position', validators=[Length(max=50)])
    position = StringField('Position', validators=[Length(max=50)])
    foot = StringField('Foot', validators=[Length(max=50)])
    height_in_cm = IntegerField('Height (cm)', validators=[NumberRange(min=0)])
    market_value_in_eur = IntegerField('Market Value (EUR)', validators=[NumberRange(min=0)])
    highest_market_value_in_eur = IntegerField('Highest Market Value (EUR)', validators=[NumberRange(min=0)])
    contract_expiration_date = StringField('Contract Expiration Date', validators=[Length(max=50)])
    submit = SubmitField('Submit')

class PlayerForm(FlaskForm):
    first_name = StringField('First Name', validators=[Length(max=50)])
    last_name = StringField('Last Name', validators=[Length(max=50)])
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=255)])
    current_club_name = StringField('Current Club Name', validators=[Length(max=40)])
    current_club_id = StringField('Current Club ID')  # Assuming it can be entered as a string
    competition_id = StringField('Competition ID', validators=[Length(max=4)])
    submit = SubmitField('Submit')
class ClubForm(FlaskForm):
    club_code = StringField('Club Code', validators=[DataRequired(), Length(min=1, max=10)])
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=255)])
    total_market_value = DecimalField('Total Market Value (EUR)', validators=[NumberRange(min=0)])
    squad_size = IntegerField('Squad Size', validators=[NumberRange(min=0)])
    average_age = DecimalField('Average Age', validators=[NumberRange(min=0)])
    foreigners_number = IntegerField('Foreigners Number', validators=[NumberRange(min=0)])
    foreigners_percentage = DecimalField('Foreigners Percentage', validators=[NumberRange(min=0, max=100)])
    national_team_players = IntegerField('National Team Players', validators=[NumberRange(min=0)])
    stadium_name = StringField('Stadium Name', validators=[Length(max=255)])
    stadium_seats = IntegerField('Stadium Seats', validators=[NumberRange(min=0)])
    net_transfer_record = DecimalField('Net Transfer Record (EUR)', validators=[NumberRange(min=0)])
    coach_name = StringField('Coach Name', validators=[Length(max=255)])
    last_season = StringField('Last Season', validators=[Length(max=10)])
    url = StringField('URL', validators=[Length(max=255)])
    submit = SubmitField('Submit')
class GameAddForm(FlaskForm):
    competition_id = StringField('Competition ID', validators=[DataRequired(), Length(max=255)])
    season = StringField('Season', validators=[Length(max=255)])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    home_club_id = IntegerField('Home Club ID', validators=[DataRequired(), NumberRange(min=1)])
    away_club_id = IntegerField('Away Club ID', validators=[DataRequired(), NumberRange(min=1)])
    home_club_goals = IntegerField('Home Club Goals', validators=[NumberRange(min=0)])
    away_club_goals = IntegerField('Away Club Goals', validators=[NumberRange(min=0)])
    home_club_position = IntegerField('Home Club Position', validators=[NumberRange(min=0)])
    away_club_position = IntegerField('Away Club Position', validators=[NumberRange(min=0)])
    home_club_manager_name = StringField('Home Club Manager Name', validators=[Length(max=255)])
    away_club_manager_name = StringField('Away Club Manager Name', validators=[Length(max=255)])
    stadium = StringField('Stadium', validators=[Length(max=255)])
    attendance = IntegerField('Attendance', validators=[NumberRange(min=0)])
    referee = StringField('Referee', validators=[Length(max=255)])
    url = StringField('URL', validators=[Length(max=255)])
    home_club_name = StringField('Home Club Name', validators=[Length(max=255)])
    away_club_name = StringField('Away Club Name', validators=[Length(max=255)])
    submit = SubmitField('Create Game')

class GameEditForm(FlaskForm):
    competition_id = StringField('Competition ID', validators=[DataRequired(), Length(max=255)])
    season = StringField('Season', validators=[Length(max=255)])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    home_club_id = IntegerField('Home Club ID', validators=[DataRequired(), NumberRange(min=1)])
    away_club_id = IntegerField('Away Club ID', validators=[DataRequired(), NumberRange(min=1)])
    home_club_goals = IntegerField('Home Club Goals', validators=[NumberRange(min=0)])
    away_club_goals = IntegerField('Away Club Goals', validators=[NumberRange(min=0)])
    home_club_position = IntegerField('Home Club Position', validators=[NumberRange(min=0)])
    away_club_position = IntegerField('Away Club Position', validators=[NumberRange(min=0)])
    home_club_manager_name = StringField('Home Club Manager Name', validators=[Length(max=255)])
    away_club_manager_name = StringField('Away Club Manager Name', validators=[Length(max=255)])
    stadium = StringField('Stadium', validators=[Length(max=255)])
    attendance = IntegerField('Attendance', validators=[NumberRange(min=0)])
    referee = StringField('Referee', validators=[Length(max=255)])
    url = StringField('URL', validators=[Length(max=255)])
    home_club_name = StringField('Home Club Name', validators=[Length(max=255)])
    away_club_name = StringField('Away Club Name', validators=[Length(max=255)])
    submit = SubmitField('Edit Game')