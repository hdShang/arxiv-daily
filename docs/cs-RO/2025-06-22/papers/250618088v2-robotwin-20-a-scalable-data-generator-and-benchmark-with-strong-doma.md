---
layout: default
title: "RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation"
---

# RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18088" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18088v2</a>
  <a href="https://arxiv.org/pdf/2506.18088.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18088v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18088v2', 'RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianxing Chen, Zanxin Chen, Baijun Chen, Zijian Cai, Yibin Liu, Zixuan Li, Qiwei Liang, Xianliang Lin, Yiheng Ge, Zhenyu Gu, Weiliang Deng, Yubin Guo, Tian Nian, Xuanbing Xie, Qiangyu Chen, Kailun Su, Tianling Xu, Guodong Liu, Mengkang Hu, Huan-ang Gao, Kaixuan Wang, Zhixuan Liang, Yusen Qin, Xiaokang Yang, Ping Luo, Yao Mu

**分类**: cs.RO, cs.AI, cs.CL, cs.CV, cs.MA

**发布日期**: 2025-06-22 (更新: 2025-08-27)

**备注**: Project Page: https://robotwin-platform.github.io/, Code: https://github.com/robotwin-Platform/robotwin, Doc: https://robotwin-platform.github.io/doc/

**🔗 代码/项目**: [GITHUB](https://github.com/robotwin-Platform/robotwin/)

---

## 💡 一句话要点

**提出RoboTwin 2.0以解决双臂机器人操作数据不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `双臂机器人` `数据合成` `领域随机化` `仿真技术` `鲁棒性研究` `多模态学习` `自动化生成`

## 📋 核心要点

1. 现有的双臂机器人操作数据集缺乏可扩展的任务生成方法，导致数据不足以支持鲁棒性研究。
2. RoboTwin 2.0通过自动化生成多样化的仿真数据，并结合领域随机化，提升了数据的多样性和策略的鲁棒性。
3. 实验结果显示，使用合成数据加上仅10个真实示例的VLA模型相较于10个示例基线提升了367%的性能。

## 📝 摘要（中文）

基于仿真的数据合成已成为推动现实世界机器人操作的重要范式。然而，现有数据集在双臂操作的鲁棒性方面仍显不足，主要由于缺乏可扩展的任务生成方法和过于简化的仿真环境。本文提出RoboTwin 2.0，一个可扩展的框架，用于自动化、大规模生成多样且真实的数据，并提供统一的双臂操作评估协议。核心是RoboTwin-OD，一个包含731个实例和147个类别的对象库，具有语义和操作相关的注释。通过多模态语言模型和仿真循环优化，自动生成任务级执行代码。RoboTwin 2.0在五个维度上应用结构化领域随机化，增强数据多样性和策略鲁棒性。实验证明，该框架在代码生成成功率上提升了10.9%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有双臂机器人操作数据集在任务生成和仿真环境简化方面的不足，导致的鲁棒性问题。

**核心思路**：RoboTwin 2.0通过构建一个可扩展的自动化数据生成框架，结合领域随机化技术，增强数据的多样性和策略的适应性。

**技术框架**：该框架包括RoboTwin-OD对象库、专家数据合成管道以及基于多模态语言模型的任务执行代码生成模块。通过结构化领域随机化，框架在五个维度上进行优化。

**关键创新**：RoboTwin 2.0的主要创新在于其结构化领域随机化方法，能够在多维度上增强数据的多样性，从而提升仿真到现实的转移能力。

**关键设计**：在数据合成过程中，采用了多模态语言模型进行任务代码生成，并通过仿真循环优化来提升生成代码的质量和执行成功率。

## 📊 实验亮点

实验结果显示，RoboTwin 2.0在代码生成成功率上提升了10.9%。使用合成数据和仅10个真实示例训练的VLA模型相较于基线提升了367%，而仅使用合成数据的零-shot模型也获得了228%的提升，显示出该框架在仿真到现实转移中的有效性。

## 🎯 应用场景

RoboTwin 2.0的研究成果可广泛应用于机器人操作、自动化制造、智能家居等领域，能够有效提升机器人在复杂环境中的操作能力和适应性，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Simulation-based data synthesis has emerged as a powerful paradigm for advancing real-world robotic manipulation. Yet existing datasets remain insufficient for robust bimanual manipulation due to (1) the lack of scalable task generation methods and (2) oversimplified simulation environments. We present RoboTwin 2.0, a scalable framework for automated, large-scale generation of diverse and realistic data, together with unified evaluation protocols for dual-arm manipulation. At its core is RoboTwin-OD, an object library of 731 instances across 147 categories with semantic and manipulation-relevant annotations. Building on this, we design an expert data synthesis pipeline that leverages multimodal language models (MLLMs) and simulation-in-the-loop refinement to automatically generate task-level execution code. To improve sim-to-real transfer, RoboTwin 2.0 applies structured domain randomization along five axes: clutter, lighting, background, tabletop height, and language, enhancing data diversity and policy robustness. The framework is instantiated across 50 dual-arm tasks and five robot embodiments. Empirically, it yields a 10.9% gain in code generation success rate. For downstream policy learning, a VLA model trained with synthetic data plus only 10 real demonstrations achieves a 367% relative improvement over the 10-demo baseline, while zero-shot models trained solely on synthetic data obtain a 228% gain. These results highlight the effectiveness of RoboTwin 2.0 in strengthening sim-to-real transfer and robustness to environmental variations. We release the data generator, benchmark, dataset, and code to support scalable research in robust bimanual manipulation. Project Page: https://robotwin-platform.github.io/, Code: https://github.com/robotwin-Platform/robotwin/.

