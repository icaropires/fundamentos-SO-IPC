#include "middleware_b.h"

int main() {
    int msqid = create_message_queue(FILE_PATH, ARB_CHAR_B);
	Message msg;
    msg.mtype = NORMAL_MESSAGE_TYPE;

	fprintf(stdout, "Middleware B started.\n", msqid);
	//fprintf(stdout, "Messages will be sent to queue with msqid %d.\n", msqid);

	do {
		strcpy(msg.msg, get_msg_from_sh_memory());
		fprintf(stdout, "Sending messsage from MIDDLEWARE B...\n");
	    sending_message(msqid, &msg, FLAG);
		fprintf(stdout, "Message sent from MIDDLEWARE B\n");
		if(strcmp(msg.msg, "EDN")) {
			break;
		}
	} while(1);

	close_sh_memory();

	return 0;
}
