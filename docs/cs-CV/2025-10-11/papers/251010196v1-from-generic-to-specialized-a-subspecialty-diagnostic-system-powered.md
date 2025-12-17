---
layout: default
title: From Generic to Specialized: A Subspecialty Diagnostic System Powered by Self-Supervised Learning for Cervical Histopathology
---

# From Generic to Specialized: A Subspecialty Diagnostic System Powered by Self-Supervised Learning for Cervical Histopathology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10196" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10196v1</a>
  <a href="https://arxiv.org/pdf/2510.10196.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10196v1" onclick="toggleFavorite(this, '2510.10196v1', 'From Generic to Specialized: A Subspecialty Diagnostic System Powered by Self-Supervised Learning for Cervical Histopathology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yizhi Wang, Li Chen, Qiang Huang, Tian Guan, Xi Deng, Zhiyuan Shen, Jiawen Li, Xinrui Chen, Bin Hu, Xitong Ling, Taojie Zhu, Zirui Huang, Deshui Yu, Yan Liu, Jiurun Chen, Lianghui Zhu, Qiming He, Yiqing Liu, Diwei Shi, Hanzhong Liu, Junbo Hu, Hongyi Gao, Zhen Song, Xilong Zhao, Chao He, Ming Zhao, Yonghong He

**分类**: cs.CV

**发布日期**: 2025-10-11

**备注**: 32 pages, 6 figures

---

## 💡 一句话要点

**CerS-Path：基于自监督学习的宫颈组织病理亚专科诊断系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `宫颈癌` `组织病理学` `自监督学习` `多模态学习` `深度学习` `亚专科诊断` `医学影像`

## 📋 核心要点

1. 现有深度学习模型在宫颈癌组织病理诊断中准确性和泛化性不足，通用基础模型难以捕捉亚专科特异性特征。
2. CerS-Path通过自监督学习和多模态增强，构建宫颈特异性特征提取器，并集成多个下游诊断功能。
3. 在3173个病例的前瞻性测试中，CerS-Path保持了99.38%的筛查敏感性和出色的泛化性，展现了临床潜力。

## 📝 摘要（中文）

宫颈癌是一种主要的恶性肿瘤，需要广泛而复杂的组织病理学评估和全面的支持工具。尽管深度学习显示出前景，但这些模型仍然缺乏准确性和泛化性。通用基础模型提供了更广泛的覆盖范围，但在捕获亚专科特定特征和任务适应性方面仍然有限。我们介绍了宫颈亚专科病理（CerS-Path）诊断系统，该系统通过两个协同预训练阶段开发：对来自14万张切片的约1.9亿个组织块进行自监督学习，以构建宫颈特异性特征提取器；以及使用250万个图像-文本对进行多模态增强，然后与多个下游诊断功能集成。CerS-Path支持包括罕见癌症分类和多模态问答在内的八个诊断功能，在范围和临床适用性方面超越了先前的基础模型。全面的评估表明，宫颈病理学取得了显著进展，在五个中心的3173个病例中进行的前瞻性测试保持了99.38%的筛查敏感性和出色的泛化性，突显了其在亚专科诊断转化和宫颈癌筛查中的潜力。

## 🔬 方法详解

**问题定义**：宫颈癌的组织病理学诊断复杂且耗时，现有深度学习方法泛化性差，无法有效处理亚专科的特定病理特征。通用基础模型虽然覆盖面广，但在特定任务上的表现仍有提升空间。因此，需要一种更准确、更具泛化能力的宫颈病理诊断系统。

**核心思路**：论文的核心思路是利用大规模的宫颈组织病理图像数据进行自监督学习，从而学习到宫颈组织特异性的特征表示。然后，通过多模态学习，将图像信息与文本描述相结合，进一步提升模型的诊断能力。这种方法旨在克服通用模型在亚专科任务上的局限性，并提高模型的准确性和泛化性。

**技术框架**：CerS-Path系统包含两个主要的预训练阶段：首先，使用自监督学习方法在大规模宫颈组织病理图像数据集上训练一个宫颈特异性的特征提取器。然后，利用图像-文本对进行多模态增强，将图像特征与文本描述信息融合。最后，将预训练的模型应用于多个下游诊断任务，例如罕见癌症分类和多模态问答。整个系统旨在提供全面的宫颈病理诊断支持。

**关键创新**：CerS-Path的关键创新在于其两阶段预训练策略，即先通过自监督学习构建宫颈特异性特征提取器，再通过多模态学习增强模型的诊断能力。这种方法不同于直接使用通用基础模型，而是针对宫颈病理的特点进行了专门的优化。此外，CerS-Path集成了多个下游诊断功能，提供了更全面的临床应用。

**关键设计**：在自监督学习阶段，论文使用了大约1.9亿个组织块进行训练，具体使用的自监督学习方法未知。在多模态增强阶段，使用了250万个图像-文本对，具体的融合方法未知。下游诊断任务包括罕见癌症分类和多模态问答等，具体的网络结构和损失函数未知。前瞻性测试在五个中心进行，使用了3173个病例。

## 📊 实验亮点

CerS-Path在3173个病例的前瞻性测试中保持了99.38%的筛查敏感性，表明其在实际临床应用中具有很高的可靠性。与先前的基础模型相比，CerS-Path在范围和临床适用性方面均有所提升，证明了其在宫颈病理诊断领域的显著优势。该系统支持八个诊断功能，包括罕见癌症分类和多模态问答，展现了其强大的功能和潜力。

## 🎯 应用场景

CerS-Path系统可应用于宫颈癌筛查、辅助诊断、病理学研究等领域。通过提高诊断准确性和效率，有望减轻病理医生的工作负担，并为患者提供更及时、更准确的诊断结果。该系统还可用于远程医疗，为缺乏病理专家的地区提供支持，具有重要的社会价值和临床意义。

## 📄 摘要（原文）

> Cervical cancer remains a major malignancy, necessitating extensive and complex histopathological assessments and comprehensive support tools. Although deep learning shows promise, these models still lack accuracy and generalizability. General foundation models offer a broader reach but remain limited in capturing subspecialty-specific features and task adaptability. We introduce the Cervical Subspecialty Pathology (CerS-Path) diagnostic system, developed through two synergistic pretraining stages: self-supervised learning on approximately 190 million tissue patches from 140,000 slides to build a cervical-specific feature extractor, and multimodal enhancement with 2.5 million image-text pairs, followed by integration with multiple downstream diagnostic functions. Supporting eight diagnostic functions, including rare cancer classification and multimodal Q&A, CerS-Path surpasses prior foundation models in scope and clinical applicability. Comprehensive evaluations demonstrate a significant advance in cervical pathology, with prospective testing on 3,173 cases across five centers maintaining 99.38% screening sensitivity and excellent generalizability, highlighting its potential for subspecialty diagnostic translation and cervical cancer screening.

