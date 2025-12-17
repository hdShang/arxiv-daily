---
layout: default
title: A Hybrid Deep Learning Framework for Emotion Recognition in Children with Autism During NAO Robot-Mediated Interaction
---

# A Hybrid Deep Learning Framework for Emotion Recognition in Children with Autism During NAO Robot-Mediated Interaction

**arXiv**: [2512.12208v1](https://arxiv.org/abs/2512.12208) | [PDF](https://arxiv.org/pdf/2512.12208.pdf)

**作者**: Indranil Bhattacharjee, Vartika Narayani Srinet, Anirudha Bhattacharjee, Braj Bhushan, Bishakh Bhattacharya

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-13

**备注**: 12 pages, journal paper

---

## 💡 一句话要点

**提出一种混合深度学习框架，用于识别自闭症儿童在NAO机器人交互中的情绪。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `自闭症谱系障碍` `情绪识别` `人机交互` `深度学习` `图卷积网络`

## 📋 核心要点

1. 现有方法难以捕捉自闭症儿童在社交互动中微妙的情绪反应，尤其是在人机交互场景下。
2. 该研究提出了一种混合深度学习模型，结合CNN和GCN，利用视觉和几何特征进行情绪识别。
3. 实验表明，该方法能有效捕捉自闭症儿童的微表情，为个性化辅助技术奠定基础。

## 📝 摘要（中文）

本研究提出了一种新颖的深度学习流程，用于识别自闭症谱系障碍（ASD）儿童在受控实验环境中，对人形机器人（NAO）呼叫名字事件的情绪反应。数据集包含从15名自闭症儿童的视频记录中提取的约50,000个面部帧。该混合模型结合了基于微调ResNet-50的卷积神经网络（CNN）和三层图卷积网络（GCN），这些网络在从MediaPipe FaceMesh地标提取的视觉和几何特征上进行训练。使用DeepFace和FER模型的加权集成，对情绪进行概率性标记，每个模型都对七种情绪类别的软标签生成做出贡献。最终分类利用通过Kullback-Leibler散度优化的融合嵌入。该方法在建模微妙的情感反应方面表现出强大的性能，并为临床和治疗性人机交互环境中自闭症儿童的情感分析提供了重要的前景，因为该流程有效地捕捉了神经多样性儿童的微表情线索，解决了自闭症特定HRI研究中的一个主要差距。这项工作代表了印度首个如此大规模的、真实的自闭症情感分析数据集和流程，使用社交机器人技术，为未来的个性化辅助技术贡献了重要的基础。

## 🔬 方法详解

**问题定义**：论文旨在解决自闭症儿童在与NAO机器人交互过程中情绪识别的难题。现有方法难以准确捕捉自闭症儿童微妙的情绪变化，尤其是在微表情层面，这限制了人机交互的有效性和个性化辅助的潜力。

**核心思路**：论文的核心思路是结合卷积神经网络（CNN）和图卷积网络（GCN）的优势，利用视觉特征和面部几何特征，更全面地捕捉自闭症儿童的情绪表达。通过融合来自不同模型的信息，提高情绪识别的准确性和鲁棒性。

**技术框架**：整体框架包括以下几个主要阶段：1) 数据采集：收集自闭症儿童与NAO机器人交互的视频数据。2) 特征提取：使用MediaPipe FaceMesh提取面部关键点，并计算几何特征。同时，使用预训练的ResNet-50提取视觉特征。3) 模型训练：训练一个混合模型，包括一个微调的ResNet-50 CNN和一个三层GCN。4) 情绪分类：使用DeepFace和FER进行概率性情绪标记，并通过加权集成生成软标签。最终使用Kullback-Leibler散度优化的融合嵌入进行分类。

**关键创新**：该研究的关键创新在于：1) 提出了一种混合CNN-GCN模型，能够同时利用视觉和几何特征进行情绪识别。2) 使用软标签和Kullback-Leibler散度优化，提高了模型的鲁棒性和泛化能力。3) 构建了一个大规模的自闭症儿童与机器人交互的情绪识别数据集。

**关键设计**：ResNet-50进行微调以适应面部表情识别任务。GCN使用三层结构，输入为面部关键点的坐标。DeepFace和FER的权重通过实验确定，以平衡它们的贡献。Kullback-Leibler散度用于优化融合嵌入，使得模型能够更好地学习不同情绪之间的差异。

## 📊 实验亮点

该研究构建了一个包含约50,000个面部帧的大规模自闭症儿童情绪识别数据集。提出的混合CNN-GCN模型在自闭症儿童情绪识别任务上表现出强大的性能，能够有效捕捉微表情，为自闭症特定的人机交互研究提供了重要的基础。

## 🎯 应用场景

该研究成果可应用于自闭症儿童的个性化辅助治疗、社交技能训练和情感支持。通过机器人实时识别儿童的情绪状态，可以为治疗师提供更准确的反馈，并为儿童提供更个性化的干预措施。此外，该技术还可用于开发更智能的社交机器人，以改善自闭症儿童的社交互动体验。

## 📄 摘要（原文）

> Understanding emotional responses in children with Autism Spectrum Disorder (ASD) during social interaction remains a critical challenge in both developmental psychology and human-robot interaction. This study presents a novel deep learning pipeline for emotion recognition in autistic children in response to a name-calling event by a humanoid robot (NAO), under controlled experimental settings. The dataset comprises of around 50,000 facial frames extracted from video recordings of 15 children with ASD. A hybrid model combining a fine-tuned ResNet-50-based Convolutional Neural Network (CNN) and a three-layer Graph Convolutional Network (GCN) trained on both visual and geometric features extracted from MediaPipe FaceMesh landmarks. Emotions were probabilistically labeled using a weighted ensemble of two models: DeepFace's and FER, each contributing to soft-label generation across seven emotion classes. Final classification leveraged a fused embedding optimized via Kullback-Leibler divergence. The proposed method demonstrates robust performance in modeling subtle affective responses and offers significant promise for affective profiling of ASD children in clinical and therapeutic human-robot interaction contexts, as the pipeline effectively captures micro emotional cues in neurodivergent children, addressing a major gap in autism-specific HRI research. This work represents the first such large-scale, real-world dataset and pipeline from India on autism-focused emotion analysis using social robotics, contributing an essential foundation for future personalized assistive technologies.

