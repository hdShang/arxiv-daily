---
layout: default
title: Dexbotic: Open-Source Vision-Language-Action Toolbox
---

# Dexbotic: Open-Source Vision-Language-Action Toolbox

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23511" target="_blank" class="toolbar-btn">arXiv: 2510.23511v1</a>
    <a href="https://arxiv.org/pdf/2510.23511.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23511v1" 
            onclick="toggleFavorite(this, '2510.23511v1', 'Dexbotic: Open-Source Vision-Language-Action Toolbox')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Bin Xie, Erjin Zhou, Fan Jia, Hao Shi, Haoqiang Fan, Haowei Zhang, Hebei Li, Jianjian Sun, Jie Bin, Junwen Huang, Kai Liu, Kaixin Liu, Kefan Gu, Lin Sun, Meng Zhang, Peilong Han, Ruitao Hao, Ruitao Zhang, Saike Huang, Songhan Xie, Tiancai Wang, Tianle Liu, Wenbin Tang, Wenqi Zhu, Yang Chen, Yingfei Liu, Yizhuang Zhou, Yu Liu, Yucheng Zhao, Yunchao Ma, Yunfei Wei, Yuxiang Chen, Ze Chen, Zeming Li, Zhao Wu, Ziheng Zhang, Ziming Liu, Ziwei Yan, Ziyu Zhang

**分类**: cs.RO

**发布日期**: 2025-10-27

**备注**: Authors are listed in alphabetical order. The official website is located at https://dexbotic.com/. Code is available at https://github.com/Dexmal/dexbotic

---

## 💡 一句话要点

**Dexbotic：开源视觉-语言-动作工具箱，助力具身智能研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `具身智能` `开源工具箱` `预训练模型` `机器人控制`

## 📋 核心要点

1. 现有VLA研究面临环境配置复杂、模型复现困难等问题，阻碍了研究效率。
2. Dexbotic工具箱提供统一的VLA研究平台，简化环境配置，支持多种VLA策略复现。
3. 该工具箱提供更强大的预训练模型，显著提升现有VLA策略的性能表现。

## 📝 摘要（中文）

本文介绍Dexbotic，一个基于PyTorch的开源视觉-语言-动作（VLA）模型工具箱。它旨在为具身智能领域的专业人士提供一站式VLA研究服务。该工具箱提供了一个代码库，支持多种主流VLA策略，允许用户仅通过一个环境设置即可复现各种VLA方法。该工具箱以实验为中心，用户只需修改Exp脚本即可快速开发新的VLA实验。此外，我们提供了更强大的预训练模型，以实现最先进VLA策略的性能显著提升。Dexbotic将持续更新，以包含更多最新的预训练基础模型和行业领先的VLA模型。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）研究面临的主要问题是环境搭建复杂、不同VLA策略的实现方式各异，导致研究人员难以快速复现已有方法并进行创新。缺乏统一的工具箱使得VLA领域的研究效率受到限制。

**核心思路**：Dexbotic的核心思路是提供一个统一的、易于使用的开源VLA工具箱，通过集成多种主流VLA策略和提供强大的预训练模型，降低VLA研究的门槛，加速VLA领域的发展。这样设计旨在让研究人员能够专注于算法创新，而不是花费大量时间在环境配置和模型复现上。

**技术框架**：Dexbotic工具箱基于PyTorch构建，提供了一套完整的VLA研究框架。该框架主要包含以下模块：1) 环境接口：用于与各种模拟环境进行交互；2) 模型库：包含多种主流VLA模型和预训练模型；3) 策略库：实现了多种VLA策略，如模仿学习、强化学习等；4) 实验管理：提供实验配置、运行和结果分析等功能。用户可以通过修改实验脚本（Exp script）来快速开发新的VLA实验。

**关键创新**：Dexbotic的关键创新在于其一站式VLA研究服务。它不仅提供了一个统一的代码库，还集成了多种主流VLA策略和强大的预训练模型。与现有方法相比，Dexbotic降低了VLA研究的门槛，加速了VLA领域的发展。此外，Dexbotic的实验中心设计使得用户可以快速开发新的VLA实验。

**关键设计**：Dexbotic的关键设计包括：1) 统一的环境接口，方便用户在不同模拟环境中进行实验；2) 模块化的模型和策略库，方便用户选择和组合不同的VLA模型和策略；3) 灵活的实验配置，允许用户自定义实验参数和评估指标；4) 强大的预训练模型，提供更好的初始化，加速模型收敛。

## 📊 实验亮点

Dexbotic提供了更强大的预训练模型，能够显著提升现有VLA策略的性能。具体性能数据和对比基线将在后续版本中提供。该工具箱的目标是持续更新，以包含更多最新的预训练基础模型和行业领先的VLA模型。

## 🎯 应用场景

Dexbotic工具箱可广泛应用于机器人控制、自动驾驶、智能家居等领域。通过该工具箱，研究人员可以更高效地开发和评估各种VLA算法，从而推动具身智能技术的发展。未来，Dexbotic有望成为VLA领域的重要基础设施，促进相关技术的普及和应用。

## 📄 摘要（原文）

> In this paper, we present Dexbotic, an open-source Vision-Language-Action (VLA) model toolbox based on PyTorch. It aims to provide a one-stop VLA research service for professionals in the field of embodied intelligence. It offers a codebase that supports multiple mainstream VLA policies simultaneously, allowing users to reproduce various VLA methods with just a single environment setup. The toolbox is experiment-centric, where the users can quickly develop new VLA experiments by simply modifying the Exp script. Moreover, we provide much stronger pretrained models to achieve great performance improvements for state-of-the-art VLA policies. Dexbotic will continuously update to include more of the latest pre-trained foundation models and cutting-edge VLA models in the industry.

