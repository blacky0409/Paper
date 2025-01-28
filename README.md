Storage snapshotting using NVMeVirt
===================================

# Idea
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

- Just copying cannot reproduce physical fragmentation

- Logical fragmentation takes many iterations / configurations / settings

- NVMeVirt를 써서 entire storage를 snapshot을 뜨는 형태로 하자
  - VPN
  - FTL을 그대로 dump뜨기 때문에 PFN fragmentation도 처리 가능


# Design
- Overview NVMeVirt

- Dump

- Restore

- Data가 있는 부분만 snapshotting
  Loading에서 superblock 관련 issue가 있어보임


# Evaluation
- Pagecache traffic도 고려해야 함


## Microbenchmark
  - Dump performance: vanilla vs valid parts only
  - Space overhead: 특정 크기의 storage를 snapshot하는데 있어 드는 추가 공간
  - [ ] Check FSFB in fs-aging:hotstorage19
  - Dynamic layout score with blktrace
  - [ ] Recursive grep test?

## Compare filesystems
[ ] Check results against fs-aging:hotstorage19
### Ext4
  - [v] sqlite
  - [-] Git: kernel build
  - [-] Rocksdb

### F2FS
  - [-] sqlite
  - %- Git
  - %- Rocksdb
