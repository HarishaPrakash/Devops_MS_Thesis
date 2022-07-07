USE devops;

CREATE TABLE  IF NOT EXISTS metrics(commit_id varchar(100),
                            commiter_name varchar(100),
                            committed_date datetime,
                            nloc integer(100),
                            nloc_added integer(100),
                            nloc_deleted integer(100),
                            change_rate DOUBLE,
                            cyclomatic_complexity integer(100),
                            effective_cylomatic_complexity DOUBLE,
                            unit_test_case integer(100),
                            failed_unit_test_case integer(100),
                            integration_test_case integer(100),
                            failed_integration_test_case integer(100),
                            production_deployment datetime
                            );