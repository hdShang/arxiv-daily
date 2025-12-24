---
layout: default
title: "DentVLM: A Multimodal Vision-Language Model for Comprehensive Dental Diagnosis and Enhanced Clinical Practice"
---

# DentVLM: A Multimodal Vision-Language Model for Comprehensive Dental Diagnosis and Enhanced Clinical Practice

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23344" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23344v1</a>
  <a href="https://arxiv.org/pdf/2509.23344.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23344v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23344v1', 'DentVLM: A Multimodal Vision-Language Model for Comprehensive Dental Diagnosis and Enhanced Clinical Practice')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zijie Meng, Jin Hao, Xiwei Dai, Yang Feng, Jiaxiang Liu, Bin Feng, Huikai Wu, Xiaotang Gai, Hengchuan Zhu, Tianxiang Hu, Yangyang Wu, Hongxia Xu, Jin Li, Jun Xiao, Xiaoqiang Liu, Joey Tianyi Zhou, Fudong Zhu, Zhihe Zhao, Lunguo Xia, Bing Fang, Jimeng Sun, Jian Wu, Zuozhu Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**DentVLM：用于全面牙科诊断和增强临床实践的多模态视觉-语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `视觉-语言模型` `牙科诊断` `临床决策支持` `医学影像` `人工智能` `视觉问答` `深度学习`

## 📋 核心要点

1. 现有AI模型难以满足牙科临床实践中复杂的多模态信息处理需求，限制了其在全面牙科诊断中的应用。
2. DentVLM通过构建大规模多模态数据集，并设计视觉-语言模型，实现了对多种牙科影像的综合理解和诊断。
3. 实验结果表明，DentVLM在多项牙科诊断任务中显著优于现有模型，并能有效提升牙医的诊断效率和准确性。

## 📝 摘要（中文）

口腔疾病的诊断和管理需要对各种影像模态进行高级视觉解释和综合信息整合。虽然目前的人工智能模型擅长孤立的任务，但它们在解决综合临床牙科实践的复杂、多模态需求方面往往不足。我们推出了DentVLM，一种专为专家级口腔疾病诊断而设计的视觉-语言模型。DentVLM是使用包含110,447张图像和246万个视觉问答（VQA）对的大规模双语数据集开发的。该模型能够解释七种2D口腔影像模态，涵盖36个诊断任务，在口腔疾病诊断方面的准确率比领先的专有和开源模型高出19.6%，在错颌畸形诊断方面的准确率高出27.9%。在一项涉及25名牙医的临床研究中，评估了1946名患者和3105个问答对，DentVLM在36项任务中的21项上超过了13名初级牙医的诊断性能，并在36项任务中的12项上超过了12名高级牙医的诊断性能。当集成到协作工作流程中时，DentVLM将初级牙医的性能提升到高级水平，并将所有从业人员的诊断时间缩短了15-22%。此外，DentVLM在三个实际应用场景中表现出良好的性能，包括家庭牙齿健康管理、医院智能诊断和多智能体协作交互。这些发现确立了DentVLM作为一个强大的临床决策支持工具，有望加强初级牙科护理，减少医患失衡，并在牙科领域普及专业医疗知识。

## 🔬 方法详解

**问题定义**：现有AI模型在牙科诊断领域面临的痛点是无法有效整合来自不同模态（如X光片、口腔照片等）的视觉信息和文本信息，导致诊断精度和效率受限。此外，现有模型在处理复杂病例和罕见疾病时表现不佳，难以满足临床需求。

**核心思路**：DentVLM的核心思路是构建一个多模态视觉-语言模型，使其能够同时理解和处理牙科影像和文本描述，从而实现更准确、更全面的诊断。该模型通过大规模数据集的训练，学习不同模态之间的关联，并利用视觉问答（VQA）任务来提升模型的推理能力。

**技术框架**：DentVLM的整体架构包含以下主要模块：1) 影像编码器：用于提取不同牙科影像模态的视觉特征。2) 文本编码器：用于提取文本描述的语义特征。3) 多模态融合模块：将视觉特征和语义特征进行融合，得到多模态表示。4) 问答模块：根据融合后的多模态表示，回答与牙科诊断相关的问题。

**关键创新**：DentVLM最重要的技术创新点在于其大规模多模态数据集的构建和模型的训练方式。该数据集包含了多种牙科影像模态和丰富的文本描述，为模型的训练提供了充足的数据支持。此外，模型采用了视觉问答（VQA）任务进行训练，使得模型能够更好地理解和推理牙科诊断相关的问题。

**关键设计**：DentVLM的关键设计包括：1) 影像编码器采用了预训练的卷积神经网络（CNN）或Transformer模型，以提取高质量的视觉特征。2) 文本编码器采用了预训练的语言模型（如BERT），以提取丰富的语义特征。3) 多模态融合模块采用了注意力机制，以更好地融合视觉特征和语义特征。4) 损失函数采用了交叉熵损失函数，以优化模型的问答性能。

## 📊 实验亮点

DentVLM在36项牙科诊断任务中，口腔疾病诊断准确率比领先的专有和开源模型高出19.6%，错颌畸形诊断准确率高出27.9%。在临床研究中，DentVLM在多项任务中超越了初级和高级牙医的诊断水平，并将诊断时间缩短了15-22%。这些结果表明，DentVLM具有显著的性能优势和临床应用价值。

## 🎯 应用场景

DentVLM具有广泛的应用前景，可用于家庭牙齿健康管理、医院智能诊断和多智能体协作交互等场景。它能够辅助牙医进行诊断，提高诊断效率和准确性，减少误诊率。此外，DentVLM还可以用于远程医疗，为偏远地区的患者提供高质量的牙科服务，从而促进医疗资源的公平分配。

## 📄 摘要（原文）

> Diagnosing and managing oral diseases necessitate advanced visual interpretation across diverse imaging modalities and integrated information synthesis. While current AI models excel at isolated tasks, they often fall short in addressing the complex, multimodal requirements of comprehensive clinical dental practice. Here we introduce DentVLM, a multimodal vision-language model engineered for expert-level oral disease diagnosis. DentVLM was developed using a comprehensive, large-scale, bilingual dataset of 110,447 images and 2.46 million visual question-answering (VQA) pairs. The model is capable of interpreting seven 2D oral imaging modalities across 36 diagnostic tasks, significantly outperforming leading proprietary and open-source models by 19.6% higher accuracy for oral diseases and 27.9% for malocclusions. In a clinical study involving 25 dentists, evaluating 1,946 patients and encompassing 3,105 QA pairs, DentVLM surpassed the diagnostic performance of 13 junior dentists on 21 of 36 tasks and exceeded that of 12 senior dentists on 12 of 36 tasks. When integrated into a collaborative workflow, DentVLM elevated junior dentists' performance to senior levels and reduced diagnostic time for all practitioners by 15-22%. Furthermore, DentVLM exhibited promising performance across three practical utility scenarios, including home-based dental health management, hospital-based intelligent diagnosis and multi-agent collaborative interaction. These findings establish DentVLM as a robust clinical decision support tool, poised to enhance primary dental care, mitigate provider-patient imbalances, and democratize access to specialized medical expertise within the field of dentistry.

