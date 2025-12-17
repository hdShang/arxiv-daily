---
layout: default
title: BoardVision: Deployment-ready and Robust Motherboard Defect Detection with YOLO+Faster-RCNN Ensemble
---

# BoardVision: Deployment-ready and Robust Motherboard Defect Detection with YOLO+Faster-RCNN Ensemble

**arXiv**: [2510.14389v1](https://arxiv.org/abs/2510.14389) | [PDF](https://arxiv.org/pdf/2510.14389.pdf)

**作者**: Brandon Hill, Kma Solaiman

---

## 💡 一句话要点

**提出BoardVision框架以解决主板组装缺陷检测问题**

**关键词**: `主板缺陷检测` `目标检测集成` `鲁棒性评估` `部署工具` `YOLO` `Faster R-CNN`

## 📋 核心要点

1. 核心问题：主板组装级缺陷检测在电子制造中未充分探索，如螺丝缺失和表面划痕
2. 方法要点：结合YOLOv7和Faster R-CNN，采用置信度-时间投票集成平衡精度与召回率
3. 实验或效果：在MiracleFactory数据集上评估，并测试了亮度、方向等扰动下的鲁棒性

## 📄 摘要（原文）

> Motherboard defect detection is critical for ensuring reliability in
> high-volume electronics manufacturing. While prior research in PCB inspection
> has largely targeted bare-board or trace-level defects, assembly-level
> inspection of full motherboards inspection remains underexplored. In this work,
> we present BoardVision, a reproducible framework for detecting assembly-level
> defects such as missing screws, loose fan wiring, and surface scratches. We
> benchmark two representative detectors - YOLOv7 and Faster R-CNN, under
> controlled conditions on the MiracleFactory motherboard dataset, providing the
> first systematic comparison in this domain. To mitigate the limitations of
> single models, where YOLO excels in precision but underperforms in recall and
> Faster R-CNN shows the reverse, we propose a lightweight ensemble,
> Confidence-Temporal Voting (CTV Voter), that balances precision and recall
> through interpretable rules. We further evaluate robustness under realistic
> perturbations including sharpness, brightness, and orientation changes,
> highlighting stability challenges often overlooked in motherboard defect
> detection. Finally, we release a deployable GUI-driven inspection tool that
> bridges research evaluation with operator usability. Together, these
> contributions demonstrate how computer vision techniques can transition from
> benchmark results to practical quality assurance for assembly-level motherboard
> manufacturing.

