---
layout: default
title: LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules
---

# LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules

**arXiv**: [2511.21042v1](https://arxiv.org/abs/2511.21042) | [PDF](https://arxiv.org/pdf/2511.21042.pdf)

**作者**: Cheng Yang, Hui Jin, Xinlei Yu, Zhipeng Wang, Yaoqun Liu, Fenglei Fan, Dajiang Lei, Gangyong Jia, Changmiao Wang, Ruiquan Ge

---

## 💡 一句话要点

**提出LungNoduleAgent多智能体系统以提升肺结节诊断精度**

**关键词**: `肺结节诊断` `多智能体系统` `CT图像分析` `医学影像` `智能体协作` `恶性分级`

## 📋 核心要点

1. 核心问题：现有模型在肺结节形态描述和医学知识整合方面存在不足，影响临床可靠性。
2. 方法要点：系统采用三模块协作，包括结节定位、CT报告生成和恶性推理，结合病理知识库。
3. 实验或效果：在多个数据集上测试，性能优于主流视觉语言模型和专家模型。

## 📄 摘要（原文）

> Diagnosing lung cancer typically involves physicians identifying lung nodules in Computed tomography (CT) scans and generating diagnostic reports based on their morphological features and medical expertise. Although advancements have been made in using multimodal large language models for analyzing lung CT scans, challenges remain in accurately describing nodule morphology and incorporating medical expertise. These limitations affect the reliability and effectiveness of these models in clinical settings. Collaborative multi-agent systems offer a promising strategy for achieving a balance between generality and precision in medical applications, yet their potential in pathology has not been thoroughly explored. To bridge these gaps, we introduce LungNoduleAgent, an innovative collaborative multi-agent system specifically designed for analyzing lung CT scans. LungNoduleAgent streamlines the diagnostic process into sequential components, improving precision in describing nodules and grading malignancy through three primary modules. The first module, the Nodule Spotter, coordinates clinical detection models to accurately identify nodules. The second module, the Radiologist, integrates localized image description techniques to produce comprehensive CT reports. Finally, the Doctor Agent System performs malignancy reasoning by using images and CT reports, supported by a pathology knowledge base and a multi-agent system framework. Extensive testing on two private datasets and the public LIDC-IDRI dataset indicates that LungNoduleAgent surpasses mainstream vision-language models, agent systems, and advanced expert models. These results highlight the importance of region-level semantic alignment and multi-agent collaboration in diagnosing nodules. LungNoduleAgent stands out as a promising foundational tool for supporting clinical analyses of lung nodules.

