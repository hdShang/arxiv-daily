---
layout: default
title: AutoMat: Enabling Automated Crystal Structure Reconstruction from Microscopy via Agentic Tool Use
---

# AutoMat: Enabling Automated Crystal Structure Reconstruction from Microscopy via Agentic Tool Use

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12650" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12650v1</a>
  <a href="https://arxiv.org/pdf/2505.12650.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12650v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12650v1', 'AutoMat: Enabling Automated Crystal Structure Reconstruction from Microscopy via Agentic Tool Use')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaotian Yang, Yiwen Tang, Yizhe Chen, Xiao Chen, Jiangjie Qiu, Hao Xiong, Haoyu Yin, Zhiyao Luo, Yifei Zhang, Sijia Tao, Wentao Li, Qinghua Zhang, Yuqiang Li, Wanli Ouyang, Bin Zhao, Xiaonan Wang, Fei Wei

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-19

**备注**: The code and dataset are publicly available at https://github.com/yyt-2378/AutoMat and https://huggingface.co/datasets/yaotianvector/STEM2Mat

**🔗 代码/项目**: [GITHUB](https://github.com/yyt-2378/AutoMat) | [HUGGINGFACE](https://huggingface.co/datasets/yaotianvector)

---

## 💡 一句话要点

**提出AutoMat以解决显微镜图像转化为晶体结构的挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `晶体结构重建` `扫描透射电子显微镜` `机器学习` `物理性质预测` `自动化管道` `多模态学习` `材料科学`

## 📋 核心要点

1. 现有方法在将电子显微镜图像转化为可用于模拟的晶体结构时，面临劳动强度高和易出错的问题。
2. AutoMat通过自动化处理流程，结合多种技术模块，能够高效地将STEM图像转化为原子结构并预测物理性质。
3. 在大规模实验中，AutoMat在结构匹配成功率、形成能均方根误差等指标上显著优于现有方法，验证了其有效性。

## 📝 摘要（中文）

基于机器学习的原子间势能和力场依赖于准确的原子结构，但由于实验解析晶体的稀缺性，这类数据十分有限。尽管原子分辨率电子显微镜提供了潜在的结构数据来源，但将这些图像转换为可用于模拟的格式仍然是一个劳动密集且易出错的过程，成为模型训练和验证的瓶颈。本文介绍了AutoMat，一个端到端的代理辅助管道，能够自动将扫描透射电子显微镜（STEM）图像转化为原子晶体结构，并预测其物理性质。AutoMat结合了模式自适应去噪、物理引导模板检索、对称感知原子重建、快速放松和通过MatterSim的属性预测，并在所有阶段进行协调。我们提出了首个专用的STEM2Mat-Bench进行评估，结果表明AutoMat在450个结构样本的大规模实验中显著优于现有的多模态大型语言模型和工具。

## 🔬 方法详解

**问题定义**：本文旨在解决将扫描透射电子显微镜（STEM）图像转化为原子晶体结构的挑战，现有方法在这一过程中劳动强度高且易出错，限制了数据的获取和模型的训练。

**核心思路**：AutoMat的核心思路是构建一个端到端的自动化管道，通过多种技术手段集成，实现从图像到结构的高效转化，减少人工干预和错误。

**技术框架**：AutoMat的整体架构包括模式自适应去噪、物理引导模板检索、对称感知原子重建、快速放松和属性预测等多个模块，确保各阶段的协调与高效。

**关键创新**：AutoMat的主要创新在于其代理辅助的自动化流程，首次实现了文本驱动的语言模型在此领域的超越，形成闭环推理机制。

**关键设计**：在设计中，AutoMat采用了特定的损失函数和网络结构，以优化图像处理和结构重建的精度，同时引入了STEM2Mat-Bench作为评估标准，确保了结果的可靠性。

## 📊 实验亮点

在450个结构样本的大规模实验中，AutoMat在晶格均方根偏差和形成能均方根误差等指标上显著优于现有的多模态大型语言模型，验证了其在晶体结构重建中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括材料科学、纳米技术和晶体工程等，能够为新材料的设计与优化提供重要的结构数据支持。未来，AutoMat有望推动显微镜技术与原子级模拟的结合，促进材料研究的进展。

## 📄 摘要（原文）

> Machine learning-based interatomic potentials and force fields depend critically on accurate atomic structures, yet such data are scarce due to the limited availability of experimentally resolved crystals. Although atomic-resolution electron microscopy offers a potential source of structural data, converting these images into simulation-ready formats remains labor-intensive and error-prone, creating a bottleneck for model training and validation. We introduce AutoMat, an end-to-end, agent-assisted pipeline that automatically transforms scanning transmission electron microscopy (STEM) images into atomic crystal structures and predicts their physical properties. AutoMat combines pattern-adaptive denoising, physics-guided template retrieval, symmetry-aware atomic reconstruction, fast relaxation and property prediction via MatterSim, and coordinated orchestration across all stages. We propose the first dedicated STEM2Mat-Bench for this task and evaluate performance using lattice RMSD, formation energy MAE, and structure-matching success rate. By orchestrating external tool calls, AutoMat enables a text-only LLM to outperform vision-language models in this domain, achieving closed-loop reasoning throughout the pipeline. In large-scale experiments over 450 structure samples, AutoMat substantially outperforms existing multimodal large language models and tools. These results validate both AutoMat and STEM2Mat-Bench, marking a key step toward bridging microscopy and atomistic simulation in materials science.The code and dataset are publicly available at https://github.com/yyt-2378/AutoMat and https://huggingface.co/datasets/yaotianvector/STEM2Mat.

