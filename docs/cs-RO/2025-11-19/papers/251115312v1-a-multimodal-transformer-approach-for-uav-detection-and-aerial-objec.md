---
layout: default
title: A Multimodal Transformer Approach for UAV Detection and Aerial Object Recognition Using Radar, Audio, and Video Data
---

# A Multimodal Transformer Approach for UAV Detection and Aerial Object Recognition Using Radar, Audio, and Video Data

**arXiv**: [2511.15312v1](https://arxiv.org/abs/2511.15312) | [PDF](https://arxiv.org/pdf/2511.15312.pdf)

**作者**: Mauro Larrat, Claudomiro Sales

---

## 💡 一句话要点

**提出多模态Transformer模型，融合雷达、视频和音频数据以解决无人机检测与空中物体识别问题。**

**关键词**: `多模态融合` `Transformer架构` `无人机检测` `空中物体识别` `实时系统` `特征学习`

## 📋 核心要点

1. 核心问题：单模态方法在无人机检测和空中物体识别中存在局限性，需提升鲁棒性。
2. 方法要点：设计Transformer架构，通过自注意力机制融合雷达、RGB视频、红外视频和音频特征。
3. 实验或效果：在独立测试集上准确率达0.9812，F1分数0.9826，推理速度41.11 FPS，适合实时应用。

## 📄 摘要（原文）

> Unmanned aerial vehicle (UAV) detection and aerial object recognition are critical for modern surveillance and security, prompting a need for robust systems that overcome limitations of single-modality approaches. This research addresses these challenges by designing and rigorously evaluating a novel multimodal Transformer model that integrates diverse data streams: radar, visual band video (RGB), infrared (IR) video, and audio. The architecture effectively fuses distinct features from each modality, leveraging the Transformer's self-attention mechanisms to learn comprehensive, complementary, and highly discriminative representations for classification. The model demonstrated exceptional performance on an independent test set, achieving macro-averaged metrics of 0.9812 accuracy, 0.9873 recall, 0.9787 precision, 0.9826 F1-score, and 0.9954 specificity. Notably, it exhibited particularly high precision and recall in distinguishing drones from other aerial objects. Furthermore, computational analysis confirmed its efficiency, with 1.09 GFLOPs, 1.22 million parameters, and an inference speed of 41.11 FPS, highlighting its suitability for real-time applications. This study presents a significant advancement in aerial object classification, validating the efficacy of multimodal data fusion via a Transformer architecture for achieving state-of-the-art performance, thereby offering a highly accurate and resilient solution for UAV detection and monitoring in complex airspace.

