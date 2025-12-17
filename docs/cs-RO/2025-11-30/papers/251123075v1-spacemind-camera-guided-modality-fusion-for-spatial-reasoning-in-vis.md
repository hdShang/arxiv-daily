---
layout: default
title: SpaceMind: Camera-Guided Modality Fusion for Spatial Reasoning in Vision-Language Models
---

# SpaceMind: Camera-Guided Modality Fusion for Spatial Reasoning in Vision-Language Models

**arXiv**: [2511.23075v1](https://arxiv.org/abs/2511.23075) | [PDF](https://arxiv.org/pdf/2511.23075.pdf)

**作者**: Ruosen Zhao, Zhikang Zhang, Jialei Xu, Jiahao Chang, Dong Chen, Lingyun Li, Weijian Sun, Zizhuang Wei

---

## 💡 一句话要点

**提出SpaceMind模型，通过相机引导模态融合增强视觉语言模型的空间推理能力**

**关键词**: `空间推理` `视觉语言模型` `相机引导融合` `模态融合` `3D感知`

## 📋 核心要点

1. 核心问题：现有视觉语言模型在3D空间推理（如距离估计）上表现不足，依赖辅助3D信息或浅层特征融合
2. 方法要点：采用双编码器架构，引入相机引导模态融合模块，将相机表示作为主动引导模态进行深度融合
3. 实验或效果：在VSI-Bench、SQA3D和SPBench基准上取得新最优结果，超越开放和专有系统

## 📄 摘要（原文）

> Large vision-language models (VLMs) show strong multimodal understanding but still struggle with 3D spatial reasoning, such as distance estimation, size comparison, and cross-view consistency. Existing 3D-aware methods either depend on auxiliary 3D information or enhance RGB-only VLMs with geometry encoders through shallow feature fusion. We propose SpaceMind, a multimodal large language model explicitly designed for spatial reasoning solely from RGB inputs. The model adopts a dual-encoder architecture, integrating VGGT as a spatial understanding encoder and InternViT as a 2D visual encoder. The key idea is to treat the camera representation as an active guiding modality rather than passive metadata. Specifically, SpaceMind introduces a lightweight Camera-Guided Modality Fusion module before the language model to replace shallow fusion. It applies camera-conditioned biasing to spatial tokens, assigns query-independent weights reflecting their geometric importance, and uses the camera embedding to gate the fused representation. Empirically, SpaceMind establishes new state-of-the-art results on VSI-Bench, SQA3D and SPBench, surpassing both open and proprietary systems on VSI-Bench and SPBench by large margins and achieving state-of-the-art performance on SQA3D. These results demonstrate that camera-guided modality fusion is an effective and practical inductive bias for equipping VLMs with genuinely spatially grounded intelligence. We will release code and model checkpoints to support future research.

