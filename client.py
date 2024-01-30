import grpc
import contactservice_pb2_grpc
import contactservice_pb2
import private_contact_pb2
import private_contact_pb2_grpc
import internal_contact_pb2 as internal_contact
import internal_contact_pb2_grpc
import user_pb2 as user
import contact_schema_pb2 as schema
import contact_schema_pb2_grpc
import contact_columns_pb2 as columns

import contac_common_pb2 as common


with grpc.insecure_channel("192.168.20.121:49813") as channel:
    stub = contactservice_pb2_grpc.ContactServiceStub(channel)

    response = stub.getSchema(schema.GetSchemaRequest())
    #print(response)
    #rpc getSchema(GetSchemaRequest) returns (GetSchemaResponse);


    # create a user
    try:
        response = stub.createInternalContacts(
                internal_contact.CreateInternalContactRequest(
                        user=user.User(
                                accountId=1337,
                                customerId=47),
                        contacts=[internal_contact.InternalContactCreateSetting(
                                    accountId=1,
                                    column=[columns.Column(
                                                   predefined=columns.PredefinedColumn.Value("FIRST_NAME"),
                                                   value="Test"
                                                   ),
                                            columns.Column(
                                                    predefined=columns.PredefinedColumn.Value("LAST_NAME"),
                                                    value="Test"
                                                    )
                                            ]
                                        
                                )]
                        )
                 )
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
            response = {'msg', 'invalid arg error'}
        elif e.code() == grpc.StatusCode.ALREADY_EXISTS:
            response = {'msg', 'already exists error'} 
        

    #  rpc getInternalContacts(GetInternalContactRequest) returns (GetInternalContactResponse);
    #response = stub.getInternalContacts(internal_contact_pb2.GetInternalContactRequest(user={"customerId":1337,"accountId":47}))
    print(response)


#    message GetInternalContactRequest {
#  User user = 1;
#  ContactSearch search = 2;
#  AccountFilter accountFilter = 3;
#  optional contacts.ContactResultSetting resultSetting = 4;
#}

    response = stub.getInternalContacts(internal_contact.GetInternalContactRequest(
           user=user.User(
               accountId=1337,
               customerId=47
                ),
           search=common.ContactSearch(
               contactId=[1]

                )
            ))
    print(response)

    


