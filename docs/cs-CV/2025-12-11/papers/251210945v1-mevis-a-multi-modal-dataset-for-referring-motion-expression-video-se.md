---
layout: default
title: MeViS: A Multi-Modal Dataset for Referring Motion Expression Video Segmentation
---

# MeViS: A Multi-Modal Dataset for Referring Motion Expression Video Segmentation

**arXiv**: [2512.10945v1](https://arxiv.org/abs/2512.10945) | [PDF](https://arxiv.org/pdf/2512.10945.pdf)

**作者**: Henghui Ding, Chang Liu, Shuting He, Kaining Ying, Xudong Jiang, Chen Change Loy, Yu-Gang Jiang

---

## 💡 一句话要点

**提出MeViS多模态数据集以支持基于运动表达的视频分割与理解**

**关键词**: `多模态数据集` `运动表达视频分割` `视频对象跟踪` `音频引导分割` `复杂场景理解`

## 📋 核心要点

1. 现有数据集强调静态属性，忽视运动在视频和语言中的作用
2. MeViS包含33,072条文本和音频运动表达，覆盖复杂场景中的8,171个对象
3. 基准测试显示现有方法在运动表达引导的视频理解方面存在局限，LMPM++方法取得新SOTA

## 📄 摘要（原文）

> This paper proposes a large-scale multi-modal dataset for referring motion expression video segmentation, focusing on segmenting and tracking target objects in videos based on language description of objects' motions. Existing referring video segmentation datasets often focus on salient objects and use language expressions rich in static attributes, potentially allowing the target object to be identified in a single frame. Such datasets underemphasize the role of motion in both videos and languages. To explore the feasibility of using motion expressions and motion reasoning clues for pixel-level video understanding, we introduce MeViS, a dataset containing 33,072 human-annotated motion expressions in both text and audio, covering 8,171 objects in 2,006 videos of complex scenarios. We benchmark 15 existing methods across 4 tasks supported by MeViS, including 6 referring video object segmentation (RVOS) methods, 3 audio-guided video object segmentation (AVOS) methods, 2 referring multi-object tracking (RMOT) methods, and 4 video captioning methods for the newly introduced referring motion expression generation (RMEG) task. The results demonstrate weaknesses and limitations of existing methods in addressing motion expression-guided video understanding. We further analyze the challenges and propose an approach LMPM++ for RVOS/AVOS/RMOT that achieves new state-of-the-art results. Our dataset provides a platform that facilitates the development of motion expression-guided video understanding algorithms in complex video scenes. The proposed MeViS dataset and the method's source code are publicly available at https://henghuiding.com/MeViS/

