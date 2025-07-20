CREATE TABLE test_case
(
    test_case_id     INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    task_id          INT                               NULL,
    task_description TEXT                              NULL,
    assigned_to      varchar                           NULL,
    created_date     TIMESTAMP                         NULL DEFAULT CURRENT_TIMESTAMP,
    modified_date    TIMESTAMP                         NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES task (task_id)
);