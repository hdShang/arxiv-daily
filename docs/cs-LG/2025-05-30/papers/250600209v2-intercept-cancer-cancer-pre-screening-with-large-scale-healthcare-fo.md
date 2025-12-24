---
layout: default
title: Intercept Cancer: Cancer Pre-Screening with Large Scale Healthcare Foundation Models
---

# Intercept Cancer: Cancer Pre-Screening with Large Scale Healthcare Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00209" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00209v2</a>
  <a href="https://arxiv.org/pdf/2506.00209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00209v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00209v2', 'Intercept Cancer: Cancer Pre-Screening with Large Scale Healthcare Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liwen Sun, Hao-Ren Yao, Gary Gao, Ophir Frieder, Chenyan Xiong

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-30 (更新: 2025-09-26)

---

## 💡 一句话要点

**提出CATCH-FM以解决癌症筛查效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `癌症筛查` `电子健康记录` `机器学习` `医疗大语言模型` `风险预测` `基础模型` `个性化医疗`

## 📋 核心要点

1. 现有癌症筛查方法成本高且侵入性强，无法广泛应用，导致早期发现率低。
2. CATCH-FM通过分析历史医疗记录，利用大规模健康基础模型识别高风险患者，提供了一种新的癌症预筛查方法。
3. 在三万名患者的评估中，CATCH-FM在癌症风险预测中表现优异，显著提高了预测准确性。

## 📝 摘要（中文）

癌症筛查能够早期发现疾病并挽救生命，但现有技术往往需要昂贵且侵入性的医疗程序，且在全球范围内并不普遍，导致许多本可挽救的生命失去。本文提出CATCH-FM（CATch Cancer with Healthcare Foundation Models），一种基于历史医疗记录识别高风险患者的癌症预筛查方法。通过对数百万电子健康记录（EHR）的分析，建立了EHR基础模型的扩展规律，并在临床医生策划的癌症风险预测数据集上进行了预训练和微调。CATCH-FM在三万名患者的回顾性评估中表现出色，在99%特异性阈值下实现了50%的灵敏度，且在AUPRC上超越了特征基础树模型和通用及医疗大语言模型20%。

## 🔬 方法详解

**问题定义**：现有癌症筛查方法依赖昂贵且侵入性的医疗程序，导致筛查覆盖面不足，许多高风险患者未能及时发现。

**核心思路**：CATCH-FM通过分析患者的历史医疗记录，利用大规模健康基础模型进行癌症风险预测，旨在提高筛查效率和准确性。

**技术框架**：该方法包括数据收集、模型预训练、微调和评估四个主要阶段。首先，收集大量电子健康记录（EHR）；然后，基于医疗编码序列对模型进行预训练；接着，在临床医生策划的癌症风险预测数据集上进行微调；最后，评估模型的预测性能。

**关键创新**：CATCH-FM的创新在于其利用大规模EHR数据进行预训练，且在不同患者分布下依然保持高效的预测能力，超越了传统特征基础模型。

**关键设计**：模型参数设置达到2.4亿，采用计算最优的基础模型架构，损失函数和网络结构经过精心设计，以确保在癌症风险预测中的高效性和准确性。

## 📊 实验亮点

CATCH-FM在三万名患者的评估中实现了50%的灵敏度，特异性达到99%，在AUPRC上超越了特征基础树模型和通用及医疗大语言模型，提升幅度高达20%。该方法在EHRSHOT少样本排行榜上也展现了卓越的胰腺癌风险预测能力，显示出其广泛的适用性和强大的预测性能。

## 🎯 应用场景

CATCH-FM的研究成果在癌症早期筛查领域具有广泛的应用潜力，能够帮助医疗机构在资源有限的情况下有效识别高风险患者，从而提高癌症的早期发现率，降低死亡率。未来，该方法还可扩展至其他疾病的筛查与预测，推动个性化医疗的发展。

## 📄 摘要（原文）

> Cancer screening, leading to early detection, saves lives. Unfortunately, existing screening techniques require expensive and intrusive medical procedures, not globally available, resulting in too many lost would-be-saved lives. We present CATCH-FM, CATch Cancer early with Healthcare Foundation Models, a cancer pre-screening methodology that identifies high-risk patients for further screening solely based on their historical medical records. With millions of electronic healthcare records (EHR), we establish the scaling law of EHR foundation models pretrained on medical code sequences, pretrain compute-optimal foundation models of up to 2.4 billion parameters, and finetune them on clinician-curated cancer risk prediction cohorts. In our retrospective evaluation comprising of thirty thousand patients, CATCH-FM achieves strong efficacy, with 50% sensitivity in predicting first cancer risks at 99% specificity cutoff, and outperforming feature-based tree models and both general and medical LLMs by up to 20% AUPRC. Despite significant demographic, healthcare system, and EHR coding differences, CATCH-FM achieves state-of-the-art pancreatic cancer risk prediction on the EHRSHOT few-shot leaderboard, outperforming EHR foundation models pretrained using on-site patient data. Our analysis demonstrates the robustness of CATCH-FM in various patient distributions, the benefits of operating in the ICD code space, and its ability to capture non-trivial cancer risk factors. Our code will be open-sourced.

