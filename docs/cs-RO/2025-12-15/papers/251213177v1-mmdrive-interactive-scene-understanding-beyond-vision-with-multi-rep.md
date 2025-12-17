---
layout: default
title: MMDrive: Interactive Scene Understanding Beyond Vision with Multi-representational Fusion
---

# MMDrive: Interactive Scene Understanding Beyond Vision with Multi-representational Fusion

**arXiv**: [2512.13177v1](https://arxiv.org/abs/2512.13177) | [PDF](https://arxiv.org/pdf/2512.13177.pdf)

**作者**: Minghui Hou, Wei-Hsing Huang, Shaofeng Liang, Daizong Liu, Tai-Hao Wen, Gang Wang, Runwei Guan, Weiping Ding

---

## 💡 一句话要点

**提出MMDrive多模态融合框架以解决自动驾驶中传统视觉语言模型在3D场景理解与语义融合上的局限。**

**关键词**: `多模态融合` `3D场景理解` `自动驾驶` `视觉语言模型` `跨模态抽象`

## 📋 核心要点

1. 核心问题：现有视觉语言模型受限于2D图像理解，难以感知3D空间信息并进行深度语义融合，影响复杂自动驾驶环境性能。
2. 方法要点：引入文本导向多模态调制器和跨模态抽象器，动态融合占用图、LiDAR点云和文本描述，实现自适应特征整合与关键信息提取。
3. 实验或效果：在DriveLM和NuScenes-QA基准测试中，MMDrive显著超越现有模型，如BLEU-4达54.56，准确率62.7%，提升自动驾驶场景理解能力。

## 📄 摘要（原文）

> Vision-language models enable the understanding and reasoning of complex traffic scenarios through multi-source information fusion, establishing it as a core technology for autonomous driving. However, existing vision-language models are constrained by the image understanding paradigm in 2D plane, which restricts their capability to perceive 3D spatial information and perform deep semantic fusion, resulting in suboptimal performance in complex autonomous driving environments. This study proposes MMDrive, an multimodal vision-language model framework that extends traditional image understanding to a generalized 3D scene understanding framework. MMDrive incorporates three complementary modalities, including occupancy maps, LiDAR point clouds, and textual scene descriptions. To this end, it introduces two novel components for adaptive cross-modal fusion and key information extraction. Specifically, the Text-oriented Multimodal Modulator dynamically weights the contributions of each modality based on the semantic cues in the question, guiding context-aware feature integration. The Cross-Modal Abstractor employs learnable abstract tokens to generate compact, cross-modal summaries that highlight key regions and essential semantics. Comprehensive evaluations on the DriveLM and NuScenes-QA benchmarks demonstrate that MMDrive achieves significant performance gains over existing vision-language models for autonomous driving, with a BLEU-4 score of 54.56 and METEOR of 41.78 on DriveLM, and an accuracy score of 62.7% on NuScenes-QA. MMDrive effectively breaks the traditional image-only understanding barrier, enabling robust multimodal reasoning in complex driving environments and providing a new foundation for interpretable autonomous driving scene understanding.

