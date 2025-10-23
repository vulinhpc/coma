# DATA-TESTIDS GUIDELINE — COMA

Mục tiêu: thống nhất `data-testid` cho Playwright/E2E, giảm flaky test.

## Quy ước đặt tên

- Dùng **kebab-case**: `project-table`, `project-create-btn`, `member-role-select`
- Theo dạng `feature-element[-intent]`
- Chỉ áp dụng cho **nút, input, table row, badge** cần test.

## Danh sách chuẩn (tối thiểu)

### Projects

- `projects-list-page`
- `project-table`
- `project-create-btn`
- `project-name-input`
- `project-code-input`
- `project-status-select`
- `project-save-btn`
- `project-members-tab`
- `member-add-btn`

### Daily Logs

- `dailylogs-list-page`
- `dailylog-create-btn`
- `dailylog-title-input`
- `dailylog-date-input`
- `dailylog-save-btn`

### Media

- `media-grid`
- `media-upload-btn`
- `media-item`

### Transactions

- `txn-list-page`
- `txn-create-btn`
- `txn-type-select`
- `txn-category-input`
- `txn-amount-input`
- `txn-save-btn`

### Reports

- `reports-page`
- `kpi-total-photos`
- `kpi-logs-this-month`
- `kpi-expense-this-month`
- `kpi-income-this-month`

## Mẫu sử dụng

```tsx
<>
  <Button data-testid="project-create-btn" onClick={onCreate}>New Project</Button>
  <input data-testid="project-code-input" />
  <div data-testid="media-grid">...</div>
</>
```
