---
layout: default
title: Co-speech Gesture Video Generation via Motion-Based Graph Retrieval
---

# Co-speech Gesture Video Generation via Motion-Based Graph Retrieval

**arXiv**: [2512.02576v1](https://arxiv.org/abs/2512.02576) | [PDF](https://arxiv.org/pdf/2512.02576.pdf)

**作者**: Yafei Song, Peng Zhang, Bang Zhang

---

## 💡 一句话要点

**提出基于扩散模型和运动图检索的框架以生成同步自然的语音手势视频**

**关键词**: `语音手势生成` `扩散模型` `运动图检索` `视频合成` `多对多映射`

## 📋 核心要点

1. 核心问题：语音与手势间多对多映射导致现有基于一对一映射的检索方法效果不佳
2. 方法要点：使用扩散模型学习音频与运动的联合分布生成手势，再通过运动相似性检索图路径并拼接视频
3. 实验或效果：实验验证方法在同步准确性和手势自然度上显著优于先前方法

## 📄 摘要（原文）

> Synthesizing synchronized and natural co-speech gesture videos remains a formidable challenge. Recent approaches have leveraged motion graphs to harness the potential of existing video data. To retrieve an appropriate trajectory from the graph, previous methods either utilize the distance between features extracted from the input audio and those associated with the motions in the graph or embed both the input audio and motion into a shared feature space. However, these techniques may not be optimal due to the many-to-many mapping nature between audio and gestures, which cannot be adequately addressed by one-to-one mapping. To alleviate this limitation, we propose a novel framework that initially employs a diffusion model to generate gesture motions. The diffusion model implicitly learns the joint distribution of audio and motion, enabling the generation of contextually appropriate gestures from input audio sequences. Furthermore, our method extracts both low-level and high-level features from the input audio to enrich the training process of the diffusion model. Subsequently, a meticulously designed motion-based retrieval algorithm is applied to identify the most suitable path within the graph by assessing both global and local similarities in motion. Given that not all nodes in the retrieved path are sequentially continuous, the final step involves seamlessly stitching together these segments to produce a coherent video output. Experimental results substantiate the efficacy of our proposed method, demonstrating a significant improvement over prior approaches in terms of synchronization accuracy and naturalness of generated gestures.

