CREATE TABLE task
(
    task_id                   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    project_id                INT                               NULL,
    task_description          TEXT                              NULL,
    estimate                  varchar                           NULL,
    estimated_completion_time varchar                           NULL,
    status                    varchar                           NULL,
    assigned_to               varchar                           NULL,
    task_type                 varchar                           NULL,
    created_date              TIMESTAMP                         NULL DEFAULT CURRENT_TIMESTAMP,
    modified_date             TIMESTAMP                         NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES project (project_id)
);