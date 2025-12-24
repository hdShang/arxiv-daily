---
layout: default
title: "BiND: A Neural Discriminator-Decoder for Accurate Bimanual Trajectory Prediction in Brain-Computer Interfaces"
---

# BiND: A Neural Discriminator-Decoder for Accurate Bimanual Trajectory Prediction in Brain-Computer Interfaces

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03521" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03521v1</a>
  <a href="https://arxiv.org/pdf/2509.03521.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03521v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03521v1', 'BiND: A Neural Discriminator-Decoder for Accurate Bimanual Trajectory Prediction in Brain-Computer Interfaces')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timothee Robert, MohammadAli Shaeri, Mahsa Shoaran

**分类**: q-bio.NC, cs.AI, eess.SP

**发布日期**: 2025-08-19

**备注**: Accepted for publication in IEEE Neural Engineering (NER) Conference'25

---

## 💡 一句话要点

**提出BiND以解决脑机接口中双手轨迹预测问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `脑机接口` `双手运动解码` `GRU` `神经网络` `运动预测` `时间建模` `鲁棒性` `机器学习`

## 📋 核心要点

1. 现有方法在解码双手运动时面临神经信号重叠和非线性交互的挑战，导致准确性不足。
2. BiND模型通过两阶段分类和GRU解码器结合时间索引的方式，提升了双手运动的预测精度。
3. 实验结果表明，BiND在跨会话分析中比GRU提高了多达4%的准确性，展现出更强的鲁棒性。

## 📝 摘要（中文）

从皮层内记录中解码双手运动仍然是脑机接口（BCIs）面临的关键挑战，主要由于神经表征的重叠和肢体间的非线性交互。本文提出了BiND（双手神经判别解码器），该模型分为两个阶段，首先对运动类型（单手左、单手右或双手）进行分类，然后使用基于GRU的专用解码器，结合试验相对时间索引，预测连续的二维手部速度。我们在一个来自四肢瘫痪患者的公开13次会话的皮层内数据集上，将BiND与六种最先进的模型（SVR、XGBoost、FNN、CNN、Transformer、GRU）进行了基准测试。BiND在单手和双手轨迹预测中分别达到了平均$R^2$为0.76（$	ext{±}$0.01）和0.69（$	ext{±}$0.03），在这两个任务中均超越了下一个最佳模型（GRU）2%。

## 🔬 方法详解

**问题定义**：本文旨在解决从皮层内记录中解码双手运动的准确性问题。现有方法在处理神经信号重叠和肢体间非线性交互时表现不佳，导致预测精度不足。

**核心思路**：BiND模型采用两阶段的解码策略，首先进行运动类型的分类，然后利用GRU解码器结合时间信息进行连续速度预测。这种设计旨在充分利用任务相关的特征，提高解码的准确性。

**技术框架**：BiND的整体架构分为两个主要模块：第一阶段是运动类型分类，第二阶段是基于GRU的速度预测解码器。解码器还引入了试验相对时间索引，以增强时间建模能力。

**关键创新**：BiND的主要创新在于其任务感知的判别机制和时间建模能力，这使得其在双手运动解码中表现出更高的准确性和鲁棒性，与现有方法相比具有显著的优势。

**关键设计**：在模型设计中，使用了GRU作为解码器，并引入了试验相对时间索引以增强时间特征的利用。此外，模型在训练过程中采用了适当的损失函数，以优化预测性能。

## 📊 实验亮点

BiND在单手和双手轨迹预测中分别达到了平均$R^2$为0.76和0.69，超越了GRU模型2%。在跨会话分析中，BiND的准确性提高了多达4%，展现出更强的鲁棒性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括脑机接口技术、康复机器人和人机交互系统。通过提高双手运动的解码精度，BiND能够为瘫痪患者提供更有效的运动辅助，改善其生活质量，并推动相关技术的发展。

## 📄 摘要（原文）

> Decoding bimanual hand movements from intracortical recordings remains a critical challenge for brain-computer interfaces (BCIs), due to overlapping neural representations and nonlinear interlimb interactions. We introduce BiND (Bimanual Neural Discriminator-Decoder), a two-stage model that first classifies motion type (unimanual left, unimanual right, or bimanual) and then uses specialized GRU-based decoders, augmented with a trial-relative time index, to predict continuous 2D hand velocities. We benchmark BiND against six state-of-the-art models (SVR, XGBoost, FNN, CNN, Transformer, GRU) on a publicly available 13-session intracortical dataset from a tetraplegic patient. BiND achieves a mean $R^2$ of 0.76 ($\pm$0.01) for unimanual and 0.69 ($\pm$0.03) for bimanual trajectory prediction, surpassing the next-best model (GRU) by 2% in both tasks. It also demonstrates greater robustness to session variability than all other benchmarked models, with accuracy improvements of up to 4% compared to GRU in cross-session analyses. This highlights the effectiveness of task-aware discrimination and temporal modeling in enhancing bimanual decoding.

