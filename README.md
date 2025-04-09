# Storage snapshotting using NVMeVirt

## IDEA
- As storage device performance is improved, fragmentation is influencing on storage device performance.
- Fragmentation happens at various levels of I/O stack
  - Difficult to repeatably measure - Reproducing
- No appropriate way to precisely preconditioning storage
  - As of fs-aging:sigmetrics97
    - Require long time to collect from live systems
    - Traces are large ...
  - Tools
    - tbbt:fast05 - synthetically age a disk to create a initial state for NFS trace replay
    - impressions:fast09 - synthetically age a file system by setting a small number of parameters, allowing users specify a target layout score for the resulting image
    - conway:login17

- Logical fragmentation takes many iterations / configurations / settings

- Just copying cannot reproduce physical fragmentation

- NVMeVirt를 써서 entire storage를 snapshot을 뜨는 형태로 하자
  - logical fragmentation VPN
  - FTL을 그대로 dump뜨기 때문에 PFN fragmentation도 처리 가능


### INTRODUCTION DESIGN
- 문제 제기 => 요즘은 이런게 있더라, 근데 이런게 문제가 있지 않니 ==> 조각화가 저장장치 성능에 영향을 미치고 있음 => 여기서, 우리 실험에서 시간에 따른 dynamic layout score(파일시스템의 단편화 점수=> 높을 수록 좋음), 그와 대응되게 증가하는 latency를 보여줌
- 목표 설정 => 이 문제를 이렇게 해결할 수 있지 않을까? => 뭐 여러가지가 있었는데, 근데 aging이 너무 오래걸리잖아...(fs-aging:sigmetrics97와 민석이가 측정해줄 시간에 따른 aging정도 그래프를 인용)
- 기여사항 =>  그래서 우리가 이런걸 만들었다. 우리는 이런이런 방향을 보았고, 했어 => 그래서, snapshot을 뜨자. 근데, PFN fragmentation이 문제가 되잖아 => FTL도 뜨자! => FTL 못건드는데? => 애뮬레이터 이용하자~!
- 논문 진행사항 => 논문의 구조 어디에서 ~~했다. 등


## DESIGN
- Overview NVMeVirt

- Dump

- Restore

- Data가 있는 부분만 snapshotting
  Loading에서 superblock 관련 issue가 있어보임


## EVALUATION
- Pagecache traffic도 고려해야 함


### MICROBENCHMARK
  - Dump performance: vanilla vs valid parts only
  - Space overhead: 특정 크기의 storage를 snapshot하는데 있어 드는 추가 공간
  - [ ] Check FSFB in fsaging:hotstorage19
  - Dynamic layout score with blktrace
  - [ ] Recursive grep test?


### COMPARE FILESYSTEMS
[ ] Check results against fsaging:hotstorage19
#### Ext4
  - [x] sqlite
    - 어떻게 실험
  - [x] Git: kernel build

  - [X] Rocksdb

#### F2FS
  - [x] sqlite
  - %- Git
  - %- Rocksdb

