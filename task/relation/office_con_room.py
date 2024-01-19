import hashlib
from crud_module import *

if __name__ == '__main__':
    # 회원가입
    # save_many_query = "insert into tbl_client (email, password, name) \
    #                    values(%s, %s, %s)"
    # encryption = hashlib.sha256()
    # encryption.update('9999'.encode('utf-8'))
    # save_many_params = (
    # ('hds1234@gmail.com', encryption.hexdigest(), '한동석'),
    # ('hgd1234@gmail.com', encryption.hexdigest(), '홍길동'),
    # ('lss1234@gmail.com', encryption.hexdigest(), '이순신'),
    # )
    # save_many(save_many_query, save_many_params)
    # 회사 추가
    # save_many_query = "insert into tbl_office (name, location) \
    #                    values(%s, %s)"
    # save_many_params = (
    #     ('네이버', '서울'),
    #     ('카카오', '판교'),
    #     ('구글', '종로')
    # )
    # save_many(save_many_query, save_many_params)

    # 회의실 추가
    # find_by_id_query = "select id from tbl_office where id = %s"
    # find_by_id_params = 3,
    # office = find_by_id(find_by_id_query, find_by_id_params)
    #
    # save_many_query = "insert into tbl_conference_room (office_id) \
    #                    values(%s)"
    # save_many_params = (office.get('id'),)
    # save_many(save_many_query, save_many_params)

    # 회의실마다 이용가능 시간 추가
    # find_by_id_query = "select id from tbl_conference_room where id = %s"
    # find_by_id_params = 6,
    # conference_room = find_by_id(find_by_id_query, find_by_id_params)
    # conference_room_id = conference_room.get("id")
    #
    # save_many_query = "insert into tbl_part_time (time, conference_room_id) \
    #                    values(%s, %s)"
    # save_many_params = (
    #     ('09:00:00', conference_room_id),
    #     ('12:00:00', conference_room_id),
    #     ('15:00:00', conference_room_id),
    #     ('18:00:00', conference_room_id),
    # )
    # save_many(save_many_query, save_many_params)

    # 예약 추가
    # find_all_query = "select id, name, location from tbl_office"
    # offices = find_all(find_all_query)
    # office_list = []
    #
    # for office in offices:
    #     find_all_by_query = "select id from tbl_conference_room where office_id = %s"
    #     find_all_by_params = office.get("id")
    #     conference_rooms = find_all_by(find_all_by_query, find_all_by_params)
    #     conference_room_list = []
    #
    #     for conference_room in conference_rooms:
    #         find_all_by_query = "select id, time from tbl_part_time where conference_room_id = %s"
    #         find_all_by_params = conference_room.get("id")
    #         part_times = find_all_by(find_all_by_query, find_all_by_params)
    #
    #         part_time_list = []
    #         for part_time in part_times:
    #             part_time_list.append(PartTime(part_time.get("id"), part_time.get("time")))
    #
    #         part_times = tuple(part_time_list)
    #
    #         conference_room_list.append(ConferenceRoom(conference_room.get("id"), part_times))
    #
    #     conference_rooms = tuple(conference_room_list)
    #     office_list.append(Office(office.get("id"), office.get("name"), office.get("location"), conference_rooms))
    #
    # offices = tuple(office_list)
    #
    # message = ""
    #
    # for office in offices:
    #     message += f"{office.id} {office.name} ({office.location})\n"
    #
    # office_choice = int(input(message))
    # office = offices[office_choice - 1]
    #
    # message = f"회의실 번호를 입력해주세요.\n{office.__str__()}"
    # room_choice = int(input(message))
    # conference_room = office.conference_rooms[room_choice - 1]
    #
    # find_all_by_query = "select time from tbl_reservation where conference_room_id = %s"
    # find_all_by_params = conference_room.id,
    # reservations = find_all_by(find_all_by_query, find_all_by_params)
    # conference_room.reservations = reservations
    #
    # time_choice = int(input(conference_room.__str__()))
    # part_time = conference_room.part_times[time_choice -1]
    # if part_time.status:
    #     find_by_id_query = "select email from tbl_client where email = %s"
    #     find_by_id_params = 'hds1234@gmail.com',
    #     client = find_by_id(find_by_id_query, find_by_id_params)
    #
    #     save_query = "insert into tbl_reservation(time, client_email, conference_room_id) \
    #                   values (%s, %s, %s)"
    #     save_params = part_time.__str__(), client.get("email"), conference_room.id
    #     save(save_query, save_params)
    #
    # else:
    #     print("예약 불가 회의실입니다.")

    # 회의실 전체 내용 조회(예약이 이미 완료된 회의실 시간은 보여지지 않는다).
    find_all_query = "select distinct o.id, o.name, o.location, c.id, p.time, ifnull(r.time, '예약 가능') 'r.time' \
                          from tbl_office o join tbl_conference_room c \
                          on o.id = c.office_id \
                          join tbl_part_time p \
                          on p.conference_room_id = c.id \
                          left outer join tbl_reservation r \
                          on r.conference_room_id = c.id and p.time = r.time \
                          where r.time is null"
    offices = find_all(find_all_query)

    for office in offices:
        print(
            f"{office.get('name')}, {office.get('location')}, {office.get('c.id')}번 회의실, {str(office.get('time'))}, {str(office.get('r.time'))}")


