# Apartment Chore Chart

Automated chore scheduler with SMS reminders for a 4-person apartment.

## Roommates
- **Maya, Sophie, Bri, Alizeh** — all common area chores
- **Maya, Sophie, Bri** — shared bathroom
- **Maya, Bri** — common hallway (included during their vacuum weeks)

## Chore Schedule

| Chore | Frequency | Who |
|-------|-----------|-----|
| Vacuuming (kitchen, entryway, dining, living room) | Weekly | All 4, rotating |
| Mopping (kitchen, entryway, dining room) | Monthly (every 4 weeks) | All 4, rotating |
| Stainless steel clean | Monthly (every 4 weeks) | All 4, rotating |
| Bathroom deep clean | Every 2 weeks | Maya, Sophie, Bri |

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set environment variables
```bash
export TWILIO_ACCOUNT_SID="your_sid"
export TWILIO_AUTH_TOKEN="your_token"
export TWILIO_PHONE_NUMBER="+15551234567"
```

Or copy `.env.example` to `.env` and fill in your values.

### 3. Update phone numbers
Edit `config.py` and replace the placeholder phone numbers with real ones.

### 4. Preview the schedule
```bash
python main.py preview
```

### 5. Test (dry run)
```bash
python main.py send --dry-run
```

### 6. Send for real
```bash
python main.py send
```

## Automation

Set up a cron job or GitHub Action to run every Monday morning:

```cron
# Every Monday at 9am
0 9 * * 1 cd /path/to/chore-chart && python main.py send
```

## Customizing

- **Rotation order**: Edit the `*_ROTATION` lists in `config.py`
- **Message wording**: Edit templates in `messages.py`
- **Start date**: Change `SCHEDULE_START` in `config.py`
- **Add/remove chores**: Add new rotation in `config.py`, template in `messages.py`, logic in `scheduler.py`
