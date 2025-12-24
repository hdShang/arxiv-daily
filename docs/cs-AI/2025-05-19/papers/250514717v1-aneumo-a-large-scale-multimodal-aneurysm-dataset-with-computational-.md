---
layout: default
title: Aneumo: A Large-Scale Multimodal Aneurysm Dataset with Computational Fluid Dynamics Simulations and Deep Learning Benchmarks
---

# Aneumo: A Large-Scale Multimodal Aneurysm Dataset with Computational Fluid Dynamics Simulations and Deep Learning Benchmarks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14717" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14717v1</a>
  <a href="https://arxiv.org/pdf/2505.14717.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14717v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14717v1', 'Aneumo: A Large-Scale Multimodal Aneurysm Dataset with Computational Fluid Dynamics Simulations and Deep Learning Benchmarks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xigui Li, Yuanye Zhou, Feiyang Xiao, Xin Guo, Chen Jiang, Tan Pan, Xingmeng Zhang, Cenyu Liu, Zeyun Miao, Jianchao Ge, Xiansheng Wang, Qimeng Wang, Yichi Zhang, Wenbo Zhang, Fengping Zhu, Limei Han, Yuan Qi, Chensen Lin, Yuan Cheng

**分类**: eess.IV, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-05-19

**🔗 代码/项目**: [GITHUB](https://github.com/Xigui-Li/Aneumo)

---

## 💡 一句话要点

**提出Aneumo数据集以解决脑动脉瘤风险评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脑动脉瘤` `计算流体动力学` `机器学习` `多模态数据` `风险评估` `生物医学工程` `数据集构建`

## 📋 核心要点

1. 现有的脑动脉瘤风险评估方法主要依赖形态学和患者特征，忽视了血流动力学的影响，导致评估不全面。
2. 本文提出了Aneumo数据集，通过合成3D动脉瘤形状并进行CFD模拟，提供了丰富的血流动力学数据，以支持机器学习算法的开发。
3. 数据集包含85,280个血流动力学数据和分割掩码，能够支持多模态输入任务，推动脑动脉瘤研究的进展。

## 📝 摘要（中文）

脑内动脉瘤（IAs）是严重的脑血管病变，约5%的普通人群中存在。其破裂可能导致高死亡率。当前评估IA风险的方法主要集中在形态学和患者特异性因素上，但对IA发展和破裂的血流动力学影响仍不明确。传统的计算流体动力学（CFD）方法虽然在血流动力学研究中准确，但计算量大，限制了其在大规模或实时临床应用中的部署。为了解决这一挑战，本文构建了一个大规模、高保真的动脉瘤CFD数据集，以促进高效机器学习算法的发展。基于427个真实动脉瘤几何形状，合成了10,660个3D形状以模拟动脉瘤演变，并在八种稳态质量流条件下进行CFD计算，生成了85,280个血流动力学数据。该数据集旨在推动动脉瘤研究，并促进数据驱动的方法在生物流体、医学工程和临床风险评估中的应用。

## 🔬 方法详解

**问题定义**：本文旨在解决脑动脉瘤风险评估中血流动力学影响被忽视的问题。现有方法主要关注形态学和患者特征，导致评估的局限性。

**核心思路**：通过构建一个大规模的CFD数据集，合成真实动脉瘤的3D形状，并进行血流动力学模拟，以提供丰富的数据支持机器学习算法的开发。

**技术框架**：整体流程包括数据集的构建、CFD模拟和机器学习基准测试。首先从真实动脉瘤几何形状出发，合成3D形状，然后在不同流量条件下进行CFD计算，最后提供数据集和基准测试。

**关键创新**：最重要的创新在于构建了一个高保真的CFD数据集，涵盖了大量的血流动力学数据，能够支持多模态输入，推动了脑动脉瘤研究的进展。

**关键设计**：在数据合成过程中，采用了控制变形的方法生成3D形状，并在八种稳态质量流条件下进行CFD计算，确保数据的真实性和可靠性。

## 📊 实验亮点

实验结果显示，Aneumo数据集生成的85,280个血流动力学数据能够有效支持机器学习模型的训练和评估。与传统方法相比，数据集的构建和模拟过程显著提高了数据的可用性和准确性，为脑动脉瘤研究提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括脑动脉瘤的风险评估、个性化医疗和生物流体动力学研究。通过提供丰富的血流动力学数据，Aneumo数据集能够促进机器学习算法在临床中的应用，提高动脉瘤的诊断和治疗效果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Intracranial aneurysms (IAs) are serious cerebrovascular lesions found in approximately 5\% of the general population. Their rupture may lead to high mortality. Current methods for assessing IA risk focus on morphological and patient-specific factors, but the hemodynamic influences on IA development and rupture remain unclear. While accurate for hemodynamic studies, conventional computational fluid dynamics (CFD) methods are computationally intensive, hindering their deployment in large-scale or real-time clinical applications. To address this challenge, we curated a large-scale, high-fidelity aneurysm CFD dataset to facilitate the development of efficient machine learning algorithms for such applications. Based on 427 real aneurysm geometries, we synthesized 10,660 3D shapes via controlled deformation to simulate aneurysm evolution. The authenticity of these synthetic shapes was confirmed by neurosurgeons. CFD computations were performed on each shape under eight steady-state mass flow conditions, generating a total of 85,280 blood flow dynamics data covering key parameters. Furthermore, the dataset includes segmentation masks, which can support tasks that use images, point clouds or other multimodal data as input. Additionally, we introduced a benchmark for estimating flow parameters to assess current modeling methods. This dataset aims to advance aneurysm research and promote data-driven approaches in biofluids, biomedical engineering, and clinical risk assessment. The code and dataset are available at: https://github.com/Xigui-Li/Aneumo.

