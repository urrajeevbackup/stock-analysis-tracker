# Database Schema

## users
- id (PK)
- full_name
- email (unique)
- password_hash
- is_active
- created_at

## analyses
- id (PK)
- user_id (FK -> users.id)
- stock_symbol
- stock_price
- risk_price
- reward_price
- risk_amount
- reward_amount
- risk_percent
- reward_percent
- rr_ratio
- buy_decision
- notes
- created_at

## trades
- id (PK)
- user_id (FK -> users.id)
- stock_symbol
- trade_type
- entry_price
- entry_date
- exit_price
- exit_date
- stop_loss
- target_price
- status
- notes
- created_at

## trade_trails
- id (PK)
- trade_id (FK -> trades.id)
- old_stop_loss
- new_stop_loss
- old_target_price
- new_target_price
- notes
- created_at

## uploads
- id (PK)
- entity_type
- entity_id
- file_url
- file_name
- created_at
