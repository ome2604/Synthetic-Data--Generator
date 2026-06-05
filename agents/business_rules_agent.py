class BusinessRulesAgent:

    @staticmethod
    def apply_appointment_rules(record):

        # Rule 1
        if record.get("visit_type") == "Telehealth":

            record["room_number"] = None

        # Rule 2
        if record.get("status") == "Completed":

            if not record.get("check_in_time"):
                record["check_in_time"] = (
                    record.get(
                        "appointment_datetime"
                    )
                )

            if not record.get("check_out_time"):
                record["check_out_time"] = (
                    record.get(
                        "appointment_datetime"
                    )
                )

        # Rule 3
        if record.get("status") in [
            "Cancelled",
            "No-show"
        ]:

            record["check_in_time"] = None
            record["check_out_time"] = None

        return record