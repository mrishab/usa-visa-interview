from get_visa_wait_times_response import GetVisaWaitTimesResponse
from slack_message import SlackMessage


class SlackMessageBuilder:
    def build_get_visa_wait_times(self, visa_wait_times: GetVisaWaitTimesResponse) -> SlackMessage:
        appointments = visa_wait_times.get_all()
        first_closest_appointment = appointments[0]
        second_closest_appointment = appointments[1]
        third_closest_appointment = appointments[2]

        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Visitor Visa Appointments",
                    "emoji": True
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "- *{first_city}: {first_visa_value} {first_visa_unit}*\n- {second_city}: {second_visa_value} {second_visa_unit}\n- {third_city}: {third_visa_value} {third_visa_unit}".format(
                        first_city = first_closest_appointment.city,
                        first_visa_value = first_closest_appointment.get_visitor_visa_wait_time().value,
                        first_visa_unit = first_closest_appointment.get_visitor_visa_wait_time().unit.value,
                        second_city = second_closest_appointment.city,
                        second_visa_value = second_closest_appointment.get_visitor_visa_wait_time().value,
                        second_visa_unit = second_closest_appointment.get_visitor_visa_wait_time().unit.value,
                        third_city = third_closest_appointment.city,
                        third_visa_value = third_closest_appointment.get_visitor_visa_wait_time().value,
                        third_visa_unit = third_closest_appointment.get_visitor_visa_wait_time().unit.value,
                    )
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "The closest visitor visa appointment is available in {first_city} in {first_number} {first_unit} followed by {second_city} and {third_city}".format(
                        first_city = first_closest_appointment.city,
                        first_number = first_closest_appointment.get_visitor_visa_wait_time().value,
                        first_unit = first_closest_appointment.get_visitor_visa_wait_time().unit.value,
                        second_city = second_closest_appointment.city,
                        third_city = third_closest_appointment.city
                    )
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "All NonImmigrant Appointments",
                    "emoji": True
                }
            },
            {
                "type": "divider"
            },
        ]



        for visa_wait_time in visa_wait_times.get_all():
            blocks.append({
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "{city}".format(city=visa_wait_time.city),
                    "emoji": True
                }
            })
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "{first_visa_type}: {first_visa_value} {first_visa_unit}\n{second_visa_type}: {second_visa_value} {second_visa_unit}\n{third_visa_type}: {third_visa_value} {third_visa_unit}".format(
                        first_visa_type = visa_wait_time.get_visitor_visa_wait_time().visa_type.value,
                        first_visa_value = visa_wait_time.get_visitor_visa_wait_time().value,
                        first_visa_unit = visa_wait_time.get_visitor_visa_wait_time().unit.value,
                        second_visa_type = visa_wait_time.get_student_visa_wait_time().visa_type.value,
                        second_visa_value = visa_wait_time.get_student_visa_wait_time().value,
                        second_visa_unit = visa_wait_time.get_student_visa_wait_time().unit.value,
                        third_visa_type = visa_wait_time.get_other_visa_wait_time().visa_type.value,
                        third_visa_value = visa_wait_time.get_other_visa_wait_time().value,
                        third_visa_unit = visa_wait_time.get_other_visa_wait_time().unit.value,
                    )
                }
            })

        blocks.append({
            "type": "divider"
        })
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*<https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/wait-times.html|Visit Visa Appointment Wait Times>*"
            }
        })

        return SlackMessage(text = "Visa Wait Times", blocks=blocks)
