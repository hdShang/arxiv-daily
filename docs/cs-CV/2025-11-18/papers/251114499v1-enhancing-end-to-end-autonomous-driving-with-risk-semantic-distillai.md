---
layout: default
title: Enhancing End-to-End Autonomous Driving with Risk Semantic Distillaion from VLM
---

# Enhancing End-to-End Autonomous Driving with Risk Semantic Distillaion from VLM

**arXiv**: [2511.14499v1](https://arxiv.org/abs/2511.14499) | [PDF](https://arxiv.org/pdf/2511.14499.pdf)

**作者**: Jack Qin, Zhitao Wang, Yinan Zheng, Keyu Chen, Yang Zhou, Yuanxin Zhong, Siyuan Cheng

---

## 💡 一句话要点

**提出风险语义蒸馏框架以增强端到端自动驾驶的泛化能力**

**关键词**: `自动驾驶` `风险语义蒸馏` `视觉语言模型` `端到端学习` `鸟瞰图特征` `泛化能力`

## 📋 核心要点

1. 核心问题：当前自动驾驶系统泛化能力不足，难以处理未知场景或传感器配置。
2. 方法要点：引入RiskHead模块，从视觉语言模型蒸馏风险估计到鸟瞰图特征。
3. 实验或效果：在Bench2Drive基准测试中，感知和规划能力显著提升。

## 📄 摘要（原文）

> The autonomous driving (AD) system has exhibited remarkable performance in complex driving scenarios. However, generalization is still a key limitation for the current system, which refers to the ability to handle unseen scenarios or unfamiliar sensor configurations.Related works have explored the use of Vision-Language Models (VLMs) to address few-shot or zero-shot tasks. While promising, these methods introduce a new challenge: the emergence of a hybrid AD system, where two distinct systems are used to plan a trajectory, leading to potential inconsistencies. Alternative research directions have explored Vision-Language-Action (VLA) frameworks that generate control actions from VLM directly. However, these end-to-end solutions demonstrate prohibitive computational demands. To overcome these challenges, we introduce Risk Semantic Distillation (RSD), a novel framework that leverages VLMs to enhance the training of End-to-End (E2E) AD backbones. By providing risk attention for key objects, RSD addresses the issue of generalization. Specifically, we introduce RiskHead, a plug-in module that distills causal risk estimates from Vision-Language Models into Bird's-Eye-View (BEV) features, yielding interpretable risk-attention maps.This approach allows BEV features to learn richer and more nuanced risk attention representations, which directly enhance the model's ability to handle spatial boundaries and risky objects.By focusing on risk attention, RSD aligns better with human-like driving behavior, which is essential to navigate in complex and dynamic environments. Our experiments on the Bench2Drive benchmark demonstrate the effectiveness of RSD in managing complex and unpredictable driving conditions. Due to the enhanced BEV representations enabled by RSD, we observed a significant improvement in both perception and planning capabilities.

