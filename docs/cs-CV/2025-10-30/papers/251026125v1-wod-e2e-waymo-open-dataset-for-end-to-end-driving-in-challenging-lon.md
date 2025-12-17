---
layout: default
title: WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-tail Scenarios
---

# WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-tail Scenarios

**arXiv**: [2510.26125v1](https://arxiv.org/abs/2510.26125) | [PDF](https://arxiv.org/pdf/2510.26125.pdf)

**作者**: Runsheng Xu, Hubert Lin, Wonseok Jeon, Hao Feng, Yuliang Zou, Liting Sun, John Gorman, Kate Tolstaya, Sarah Tang, Brandyn White, Ben Sapp, Mingxing Tan, Jyh-Jing Hwang, Drago Anguelov

---

## 💡 一句话要点

**提出WOD-E2E数据集和RFS指标以评估端到端驾驶在长尾场景中的性能**

**关键词**: `端到端驾驶` `长尾场景数据集` `开放环评估指标` `多模态驾驶` `自动驾驶挑战`

## 📋 核心要点

1. 当前端到端驾驶基准缺乏对长尾场景的充分测试，且评估指标难以捕捉多模态特性
2. 构建包含4021段长尾场景数据的WOD-E2E数据集，并设计基于评分者偏好的RFS评估指标
3. 通过发布验证集标签和举办挑战赛，推动鲁棒自动驾驶研究，未知具体性能提升

## 📄 摘要（原文）

> Vision-based end-to-end (E2E) driving has garnered significant interest in
> the research community due to its scalability and synergy with multimodal large
> language models (MLLMs). However, current E2E driving benchmarks primarily
> feature nominal scenarios, failing to adequately test the true potential of
> these systems. Furthermore, existing open-loop evaluation metrics often fall
> short in capturing the multi-modal nature of driving or effectively evaluating
> performance in long-tail scenarios. To address these gaps, we introduce the
> Waymo Open Dataset for End-to-End Driving (WOD-E2E). WOD-E2E contains 4,021
> driving segments (approximately 12 hours), specifically curated for challenging
> long-tail scenarios that that are rare in daily life with an occurring
> frequency of less than 0.03%. Concretely, each segment in WOD-E2E includes the
> high-level routing information, ego states, and 360-degree camera views from 8
> surrounding cameras. To evaluate the E2E driving performance on these long-tail
> situations, we propose a novel open-loop evaluation metric: Rater Feedback
> Score (RFS). Unlike conventional metrics that measure the distance between
> predicted way points and the logs, RFS measures how closely the predicted
> trajectory matches rater-annotated trajectory preference labels. We have
> released rater preference labels for all WOD-E2E validation set segments, while
> the held out test set labels have been used for the 2025 WOD-E2E Challenge.
> Through our work, we aim to foster state of the art research into
> generalizable, robust, and safe end-to-end autonomous driving agents capable of
> handling complex real-world situations.

