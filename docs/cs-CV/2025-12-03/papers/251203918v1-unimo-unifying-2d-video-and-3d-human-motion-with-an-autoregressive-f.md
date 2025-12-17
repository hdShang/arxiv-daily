---
layout: default
title: UniMo: Unifying 2D Video and 3D Human Motion with an Autoregressive Framework
---

# UniMo: Unifying 2D Video and 3D Human Motion with an Autoregressive Framework

**arXiv**: [2512.03918v1](https://arxiv.org/abs/2512.03918) | [PDF](https://arxiv.org/pdf/2512.03918.pdf)

**作者**: Youxin Pang, Yong Zhang, Ruizhi Shao, Xiang Deng, Feng Gao, Xu Xiaoming, Xiaoming Wei, Yebin Liu

---

## 💡 一句话要点

**提出UniMo以统一建模2D视频与3D人体运动，实现同时生成与理解**

**关键词**: `2D视频生成` `3D人体运动` `自回归模型` `多模态统一` `运动捕捉` `令牌序列`

## 📋 核心要点

1. 核心问题：现有方法难以统一优化和生成结构差异大的2D视频与3D运动
2. 方法要点：将视频和运动建模为统一令牌序列，设计3D运动分词器保留空间信息
3. 实验或效果：实验证明能同时生成对应视频和运动，并实现准确运动捕捉

## 📄 摘要（原文）

> We propose UniMo, an innovative autoregressive model for joint modeling of 2D human videos and 3D human motions within a unified framework, enabling simultaneous generation and understanding of these two modalities for the first time. Current methods predominantly focus on generating one modality given another as the condition or integrating either of them with other modalities such as text and audio. Unifying 2D videos and 3D motions for simultaneous optimization and generation remains largely unexplored, presenting significant challenges due to their substantial structural and distributional differences. Inspired by the LLM's ability to unify different modalities, our method models videos and 3D motions as a unified tokens sequence, utilizing separate embedding layers to mitigate distribution gaps. Additionally, we devise a sequence modeling strategy that integrates two distinct tasks within a single framework, proving the effectiveness of unified modeling. Moreover, to efficiently align with visual tokens and preserve 3D spatial information, we design a novel 3D motion tokenizer with a temporal expansion strategy, using a single VQ-VAE to produce quantized motion tokens. It features multiple expert decoders that handle body shapes, translation, global orientation, and body poses for reliable 3D motion reconstruction. Extensive experiments demonstrate that our method simultaneously generates corresponding videos and motions while performing accurate motion capture. This work taps into the capacity of LLMs to fuse diverse data types, paving the way for integrating human-centric information into existing models and potentially enabling multimodal, controllable joint modeling of humans, objects, and scenes.

