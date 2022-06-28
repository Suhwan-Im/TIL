# SSAFY RACE 코드



#### 1. 2022/06/23 AM03:10

Basic Map (2 Laps / Time: 02:15.51)

```python
        # Default Values
        car_controls.steering = 0
        car_controls.throttle = 0.85
        car_controls.brake = 0

        # Moving straight forward
        if (sensing_info.moving_angle >= -90) and (sensing_info.moving_angle <= 90):
            if (sensing_info.moving_angle >= -10) and (sensing_info.moving_angle <= 10):
                if sensing_info.to_middle < -5:
                    car_controls.steering = 0.3
                elif sensing_info.to_middle > 5:
                    car_controls.steering = -0.3
                else:
                    car_controls.steering = 0
            elif (sensing_info.moving_angle >= -90) and (sensing_info.moving_angle < -10):
                if sensing_info.to_middle < -5:
                    car_controls.steering = 0.3
                elif sensing_info.to_middle > 5:
                    car_controls.steering = -0.3
                else:
                    if sensing_info.moving_angle < -80:
                        car_controls.steering = 0.9
                        car_controls.throttle = 0.3
                        car_controls.brake = 0.5
                    elif sensing_info.moving_angle < -70:
                        car_controls.steering = 0.8
                        car_controls.throttle = 0.35
                        car_controls.brake = 0.4
                    elif sensing_info.moving_angle < -60:
                        car_controls.steering = 0.7
                        car_controls.throttle = 0.4
                        car_controls.brake = 0.3
                    elif sensing_info.moving_angle < -50:
                        car_controls.steering = 0.6
                        car_controls.throttle = 0.45
                        car_controls.brake = 0.2
                    elif sensing_info.moving_angle < -40:
                        car_controls.steering = 0.5
                        car_controls.throttle = 0.5
                        car_controls.brake = 0.1
                    elif sensing_info.moving_angle < -30:
                        car_controls.steering = 0.4
                        car_controls.throttle = 0.6
                    elif sensing_info.moving_angle < -20:
                        car_controls.steering = 0.3
                        car_controls.throttle = 0.7
                    elif sensing_info.moving_angle < -10:
                        car_controls.steering = 0.2
                        car_controls.throttle = 0.8
                    else:
                        car_controls.steering = 0
                        car_controls.throttle = 1
            elif (sensing_info.moving_angle > 10) and (sensing_info.moving_angle <= 90):
                if sensing_info.to_middle < -5:
                    car_controls.steering = 0.2
                elif sensing_info.to_middle > 5:
                    car_controls.steering = -0.2
                else:
                    if sensing_info.moving_angle > 80:
                        car_controls.steering = -0.9
                        car_controls.throttle = 0.3
                        car_controls.brake = 0.5
                    elif sensing_info.moving_angle > 70:
                        car_controls.steering = -0.8
                        car_controls.throttle = 0.35
                        car_controls.brake = 0.4
                    elif sensing_info.moving_angle > 60:
                        car_controls.steering = -0.7
                        car_controls.throttle = 0.4
                        car_controls.brake = 0.3
                    elif sensing_info.moving_angle > 50:
                        car_controls.steering = -0.6
                        car_controls.throttle = 0.45
                        car_controls.brake = 0.2
                    elif sensing_info.moving_angle > 40:
                        car_controls.steering = -0.5
                        car_controls.throttle = 0.5
                        car_controls.brake = 0.1
                    elif sensing_info.moving_angle > 30:
                        car_controls.steering = -0.4
                        car_controls.throttle = 0.6
                    elif sensing_info.moving_angle > 20:
                        car_controls.steering = -0.3
                        car_controls.throttle = 0.7
                    elif sensing_info.moving_angle > 10:
                        car_controls.steering = -0.2
                        car_controls.throttle = 0.8
                    else:
                        car_controls.steering = 0
                        car_controls.throttle = 1

        # 차량이 역주행하는 경우
        else:
            if sensing_info.speed > 20:
                car_controls.brake = 1
            else:
                car_controls.throttle = -1
                if (sensing_info.moving_angle > -180) and (sensing_info.moving_angle < -45):
                    car_controls.steering = 1
                elif (sensing_info.moving_angle > 45) and (sensing_info.moving_angle <= 180):
                    car_controls.steering = -1
                else:
                    car_controls.steering = 0
```

- 전략: 중심선을 기준으로 일정범위(5m)를 벗어나면 방향 바꿔주고, 진행방향에 상대 각도에 따라서 방향과 속도를 다르게 설정하여 트랙의 중심에 맞추어 주행하게 하려는 의도
- 문제점: 커브 구간에서 트랙을 심하게 벗어남



#### 2. 2022/06/23 PM06:05

Basic Map (2 Laps / Time: 02:32.20)

```python
    def __init__(self):
        # =========================================================== #
        #  Area for member variables =============================== #
        # =========================================================== #
        # Editing area starts from here
        #

        self.is_debug = False

        self.stuck = 0
        self.stuck_count = 0

        # api or keyboard
        self.enable_api_control = True # True(Controlled by code) /False(Controlled by keyboard)
        super().set_enable_api_control(self.enable_api_control)

        #
        # Editing area ends
        # ==========================================================#
        super().__init__()
```

```python
        # Default Values
        car_controls.steering = 0
        car_controls.throttle = 0.85
        car_controls.brake = 0

        # 멈춘경우
        if sensing_info.collided and (sensing_info.speed == 0):
            self.stuck = 1
        # 후진해서 탈출
        if self.stuck == 1:
            self.stuck_count += 1
            if self.stuck_count <= 15:
                car_controls.throttle = -1
            else:
                self.stuck = 0
                self.stuck_count = 0

        # Moving straight forward
        elif (sensing_info.moving_angle >= -90) and (sensing_info.moving_angle <= 90):
            if (sensing_info.moving_angle >= -10) and (sensing_info.moving_angle <= 10):
                if sensing_info.to_middle < -5:
                    car_controls.steering = 0.3
                elif sensing_info.to_middle > 5:
                    car_controls.steering = -0.3
                else:
                    car_controls.steering = 0
            elif (sensing_info.moving_angle >= -90) and (sensing_info.moving_angle < -10):
                if sensing_info.to_middle < -5:
                    car_controls.steering = 0.3
                elif sensing_info.to_middle > 5:
                    car_controls.steering = -0.3
                else:
                    if sensing_info.moving_angle < -80:
                        car_controls.steering = 0.9
                        car_controls.throttle = 0.3
                        car_controls.brake = 0.5
                    elif sensing_info.moving_angle < -70:
                        car_controls.steering = 0.8
                        car_controls.throttle = 0.35
                        car_controls.brake = 0.4
                    elif sensing_info.moving_angle < -60:
                        car_controls.steering = 0.7
                        car_controls.throttle = 0.4
                        car_controls.brake = 0.3
                    elif sensing_info.moving_angle < -50:
                        car_controls.steering = 0.6
                        car_controls.throttle = 0.45
                        car_controls.brake = 0.2
                    elif sensing_info.moving_angle < -40:
                        car_controls.steering = 0.5
                        car_controls.throttle = 0.5
                        car_controls.brake = 0.1
                    elif sensing_info.moving_angle < -30:
                        car_controls.steering = 0.4
                        car_controls.throttle = 0.6
                    elif sensing_info.moving_angle < -20:
                        car_controls.steering = 0.3
                        car_controls.throttle = 0.7
                    elif sensing_info.moving_angle < -10:
                        car_controls.steering = 0.2
                        car_controls.throttle = 0.8
                    else:
                        car_controls.steering = 0
                        car_controls.throttle = 1
            elif (sensing_info.moving_angle > 10) and (sensing_info.moving_angle <= 90):
                if sensing_info.to_middle < -5:
                    car_controls.steering = 0.2
                elif sensing_info.to_middle > 5:
                    car_controls.steering = -0.2
                else:
                    if sensing_info.moving_angle > 80:
                        car_controls.steering = -0.9
                        car_controls.throttle = 0.3
                        car_controls.brake = 0.5
                    elif sensing_info.moving_angle > 70:
                        car_controls.steering = -0.8
                        car_controls.throttle = 0.35
                        car_controls.brake = 0.4
                    elif sensing_info.moving_angle > 60:
                        car_controls.steering = -0.7
                        car_controls.throttle = 0.4
                        car_controls.brake = 0.3
                    elif sensing_info.moving_angle > 50:
                        car_controls.steering = -0.6
                        car_controls.throttle = 0.45
                        car_controls.brake = 0.2
                    elif sensing_info.moving_angle > 40:
                        car_controls.steering = -0.5
                        car_controls.throttle = 0.5
                        car_controls.brake = 0.1
                    elif sensing_info.moving_angle > 30:
                        car_controls.steering = -0.4
                        car_controls.throttle = 0.6
                    elif sensing_info.moving_angle > 20:
                        car_controls.steering = -0.3
                        car_controls.throttle = 0.7
                    elif sensing_info.moving_angle > 10:
                        car_controls.steering = -0.2
                        car_controls.throttle = 0.8
                    else:
                        car_controls.steering = 0
                        car_controls.throttle = 1

        # 차량이 역주행하는 경우
        else:
            if sensing_info.speed > 20:
                car_controls.brake = 1
            else:
                car_controls.throttle = -1
                if (sensing_info.moving_angle > -180) and (sensing_info.moving_angle < -45):
                    car_controls.steering = 1
                elif (sensing_info.moving_angle > 45) and (sensing_info.moving_angle <= 180):
                    car_controls.steering = -1
                else:
                    car_controls.steering = 0
```

- 장애물에 걸려서 안움직이는 경우, 후진으로 빠져나오는 코드 구현



#### 2. 2022/06/27 PM09:00

Basic Map (2 Laps / Time: 02:31.62)

```python
    def __init__(self):
        # =========================================================== #
        #  Area for member variables =============================== #
        # =========================================================== #
        # Editing area starts from here
        #

        self.is_debug = False

        self.stuck = 0
        self.stuck_count = 0

        # api or keyboard
        self.enable_api_control = True # True(Controlled by code) /False(Controlled by keyboard)
        super().set_enable_api_control(self.enable_api_control)

        #
        # Editing area ends
        # ==========================================================#
        super().__init__()
```

```python
        # Default Values
        car_controls.steering = 0
        car_controls.throttle = 0.85
        car_controls.brake = 0

        # 멈춘경우
        if sensing_info.collided and (sensing_info.speed == 0):
            self.stuck = 1
        # 후진해서 탈출
        if self.stuck == 1:
            self.stuck_count += 1
            if self.stuck_count <= 15:
                car_controls.throttle = -1
            else:
                self.stuck = 0
                self.stuck_count = 0

        # Moving straight forward
        elif (sensing_info.moving_angle >= -90) and (sensing_info.moving_angle <= 90):
            if (sensing_info.moving_angle >= -10) and (sensing_info.moving_angle <= 10):
                if sensing_info.to_middle < -5:
                    car_controls.steering = 0.3
                elif sensing_info.to_middle > 5:
                    car_controls.steering = -0.3
                else:
                    car_controls.steering = 0
            elif (sensing_info.moving_angle >= -90) and (sensing_info.moving_angle < -10):
                if sensing_info.to_middle < -5:
                    car_controls.steering = 0.3
                elif sensing_info.to_middle > 5:
                    car_controls.steering = -0.3
                else:
                    if sensing_info.moving_angle < -80:
                        car_controls.steering = 0.9
                        car_controls.throttle = 0.3
                        car_controls.brake = 0.8
                    elif sensing_info.moving_angle < -70:
                        car_controls.steering = 0.8
                        car_controls.throttle = 0.35
                        car_controls.brake = 0.4
                    elif sensing_info.moving_angle < -60:
                        car_controls.steering = 0.7
                        car_controls.throttle = 0.4
                        car_controls.brake = 0.3
                    elif sensing_info.moving_angle < -50:
                        car_controls.steering = 0.6
                        car_controls.throttle = 0.45
                        car_controls.brake = 0.2
                    elif sensing_info.moving_angle < -40:
                        car_controls.steering = 0.5
                        car_controls.throttle = 0.5
                        car_controls.brake = 0.1
                    elif sensing_info.moving_angle < -30:
                        car_controls.steering = 0.4
                        car_controls.throttle = 0.6
                    elif sensing_info.moving_angle < -20:
                        car_controls.steering = 0.3
                        car_controls.throttle = 0.7
                    elif sensing_info.moving_angle < -10:
                        car_controls.steering = 0.2
                        car_controls.throttle = 0.8
                    else:
                        car_controls.steering = 0
                        car_controls.throttle = 1
            elif (sensing_info.moving_angle > 10) and (sensing_info.moving_angle <= 90):
                if sensing_info.to_middle < -5:
                    car_controls.steering = 0.2
                elif sensing_info.to_middle > 5:
                    car_controls.steering = -0.2
                else:
                    if sensing_info.moving_angle > 80:
                        car_controls.steering = -0.9
                        car_controls.throttle = 0.3
                        car_controls.brake = 0.8
                    elif sensing_info.moving_angle > 70:
                        car_controls.steering = -0.8
                        car_controls.throttle = 0.35
                        car_controls.brake = 0.4
                    elif sensing_info.moving_angle > 60:
                        car_controls.steering = -0.7
                        car_controls.throttle = 0.4
                        car_controls.brake = 0.3
                    elif sensing_info.moving_angle > 50:
                        car_controls.steering = -0.6
                        car_controls.throttle = 0.45
                        car_controls.brake = 0.2
                    elif sensing_info.moving_angle > 40:
                        car_controls.steering = -0.5
                        car_controls.throttle = 0.5
                        car_controls.brake = 0.1
                    elif sensing_info.moving_angle > 30:
                        car_controls.steering = -0.4
                        car_controls.throttle = 0.6
                    elif sensing_info.moving_angle > 20:
                        car_controls.steering = -0.3
                        car_controls.throttle = 0.7
                    elif sensing_info.moving_angle > 10:
                        car_controls.steering = -0.2
                        car_controls.throttle = 0.8
                    else:
                        car_controls.steering = 0
                        car_controls.throttle = 1

        # 차량이 역주행하는 경우
        else:
            if sensing_info.speed > 20:
                car_controls.brake = 1
            else:
                car_controls.throttle = -1
                if (sensing_info.moving_angle > -180) and (sensing_info.moving_angle < -45):
                    car_controls.steering = 1
                elif (sensing_info.moving_angle > 45) and (sensing_info.moving_angle <= 180):
                    car_controls.steering = -1
                else:
                    car_controls.steering = 0
```

- 서버주행시, 첫번째바퀴 끝날때 골인지점을 통과하지 않아서 총 3바퀴를 도는 문제 수정