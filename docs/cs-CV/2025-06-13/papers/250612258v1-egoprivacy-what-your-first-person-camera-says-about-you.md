---
layout: default
title: "EgoPrivacy: What Your First-Person Camera Says About You?"
---

# EgoPrivacy: What Your First-Person Camera Says About You?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12258" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12258v1</a>
  <a href="https://arxiv.org/pdf/2506.12258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12258v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12258v1', 'EgoPrivacy: What Your First-Person Camera Says About You?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijiang Li, Genpei Zhang, Jiacheng Cheng, Yi Li, Xiaojun Shan, Dashan Gao, Jiancheng Lyu, Yuan Li, Ning Bi, Nuno Vasconcelos

**分类**: cs.CV, cs.CY

**发布日期**: 2025-06-13

**备注**: ICML 2025

**🔗 代码/项目**: [GITHUB](https://github.com/williamium3000/ego-privacy)

---

## 💡 一句话要点

**提出EgoPrivacy以评估第一人称视频的隐私风险**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私保护` `可穿戴摄像机` `第一人称视频` `隐私风险评估` `检索增强攻击` `基础模型` `自我中心视觉`

## 📋 核心要点

1. 现有研究对可穿戴摄像机佩戴者的隐私威胁关注不足，未能全面评估第一人称视频可能泄露的信息。
2. 提出EgoPrivacy基准，涵盖三种隐私类型，定义七个任务以恢复佩戴者的私人信息，强调隐私风险。
3. 实验结果显示，基础模型在零样本条件下可高效恢复佩戴者的身份、性别等信息，准确率达到70-80%。

## 📝 摘要（中文）

随着可穿戴摄像机的快速普及，关于第一人称视频隐私的担忧日益增加，但现有研究对摄像机佩戴者所面临的独特隐私威胁关注不足。本文探讨了一个核心问题：从佩戴者的第一人称视角视频中可以推断出多少隐私信息。我们引入了EgoPrivacy，这是第一个大规模基准，用于全面评估自我中心视觉中的隐私风险。EgoPrivacy涵盖三种隐私类型（人口统计、个体和情境），定义了七个任务，旨在恢复从细粒度（如佩戴者身份）到粗粒度（如年龄组）的私人信息。此外，我们提出了检索增强攻击，这是一种新颖的攻击策略，利用外部池中的外部视频进行自我到外部的检索，以增强人口统计隐私攻击的有效性。我们的研究表明，佩戴者的私人信息极易泄露，基础模型在零样本设置下也能有效恢复身份、场景、性别和种族等属性，准确率达到70-80%。

## 🔬 方法详解

**问题定义**：本文旨在解决可穿戴摄像机佩戴者隐私信息泄露的问题。现有方法未能充分考虑第一人称视频对佩戴者隐私的威胁，缺乏系统的评估基准。

**核心思路**：我们提出EgoPrivacy基准，通过定义多种隐私任务，系统评估佩戴者隐私信息的泄露风险，强调自我中心视觉的隐私威胁。

**技术框架**：EgoPrivacy基准包括三种隐私类型（人口统计、个体和情境），并设计了七个任务来恢复不同层次的私人信息。我们还提出了检索增强攻击策略，利用外部视频数据提升攻击效果。

**关键创新**：最重要的创新在于引入了检索增强攻击策略，通过外部视频的检索来增强隐私攻击的有效性，这在现有研究中尚属首次。

**关键设计**：在任务设计中，我们设置了多种隐私恢复任务，采用了基础模型进行实验，确保在零样本条件下也能有效评估佩戴者的隐私信息恢复能力。实验中使用的损失函数和网络结构经过精心选择，以提高准确性和鲁棒性。

## 📊 实验亮点

实验结果表明，基础模型在零样本设置下能够以70-80%的准确率恢复佩戴者的身份、场景、性别和种族等信息，显示出佩戴者隐私信息的高度泄露风险。与现有方法相比，检索增强攻击显著提升了隐私攻击的有效性，展示了EgoPrivacy基准的实用性与重要性。

## 🎯 应用场景

该研究的潜在应用领域包括可穿戴设备的隐私保护、视频监控系统的安全性评估以及社交媒体内容的隐私管理。通过系统评估隐私风险，能够为相关技术的设计和政策制定提供重要参考，促进用户隐私的保护与安全。未来，该研究可能推动更多针对隐私保护的技术创新与应用。

## 📄 摘要（原文）

> While the rapid proliferation of wearable cameras has raised significant concerns about egocentric video privacy, prior work has largely overlooked the unique privacy threats posed to the camera wearer. This work investigates the core question: How much privacy information about the camera wearer can be inferred from their first-person view videos? We introduce EgoPrivacy, the first large-scale benchmark for the comprehensive evaluation of privacy risks in egocentric vision. EgoPrivacy covers three types of privacy (demographic, individual, and situational), defining seven tasks that aim to recover private information ranging from fine-grained (e.g., wearer's identity) to coarse-grained (e.g., age group). To further emphasize the privacy threats inherent to egocentric vision, we propose Retrieval-Augmented Attack, a novel attack strategy that leverages ego-to-exo retrieval from an external pool of exocentric videos to boost the effectiveness of demographic privacy attacks. An extensive comparison of the different attacks possible under all threat models is presented, showing that private information of the wearer is highly susceptible to leakage. For instance, our findings indicate that foundation models can effectively compromise wearer privacy even in zero-shot settings by recovering attributes such as identity, scene, gender, and race with 70-80% accuracy. Our code and data are available at https://github.com/williamium3000/ego-privacy.

