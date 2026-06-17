def solution(video_len, pos, op_start, op_end, commands):
    # 1. 모든 시간을 '초(seconds)' 단위로 변환
    def to_seconds(time_str):
        mm, ss = map(int, time_str.split(":"))
        return mm * 60 + ss

    current = to_seconds(pos)
    op_s = to_seconds(op_start)
    op_e = to_seconds(op_end)
    video_limit = to_seconds(video_len)

    # 오프닝 건너뛰기 로직을 함수로 분리 (반복 사용됨)
    def skip_opening(pos_sec):
        if op_s <= pos_sec <= op_e:
            return op_e
        return pos_sec

    # 2. [시작 직후] 오프닝 구간인지 확인
    current = skip_opening(current)

    # 3. 명령어 수행
    for cmd in commands:
        if cmd == "prev":
            current = max(0, current - 10)  # 0초 미만으로 떨어지는 것 방지
        elif cmd == "next":
            current = min(video_limit, current + 10)  # 비디오 총 길이를 넘는 것 방지
        
        # [이동 후] 오프닝 구간인지 다시 확인
        current = skip_opening(current)

    # 4. "mm:ss" 형식으로 변환 (f-string의 :02d를 쓰면 한 자리 수일 때 0이 붙습니다)
    mm = current // 60
    ss = current % 60
    
    return f"{mm:02d}:{ss:02d}"
  # 처음에 문자열을 초단위 int형으로 바꿔서 계산한 것은 잘함.
  # 그러나 오프닝 건너뛰기 로직을 제대로 읽지 못해서 지속적으로 오류가 발생했고 다른 if문 코드들을 잡고 늘어졌음.
  #문제 제대로 읽어보기.
