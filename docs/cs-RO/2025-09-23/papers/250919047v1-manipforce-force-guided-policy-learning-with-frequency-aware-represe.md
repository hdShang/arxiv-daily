---
layout: default
title: "ManipForce: Force-Guided Policy Learning with Frequency-Aware Representation for Contact-Rich Manipulation"
---

# ManipForce: Force-Guided Policy Learning with Frequency-Aware Representation for Contact-Rich Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19047" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19047v1</a>
  <a href="https://arxiv.org/pdf/2509.19047.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19047v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19047v1', 'ManipForce: Force-Guided Policy Learning with Frequency-Aware Representation for Contact-Rich Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Geonhyup Lee, Yeongjin Lee, Kangmin Kim, Seongju Lee, Sangjun Noh, Seunghyeok Back, Kyoobin Lee

**分类**: cs.RO

**发布日期**: 2025-09-23

**备注**: 9 pages, 9 figures

---

## 💡 一句话要点

**ManipForce：提出力引导的策略学习方法，用于接触式操作任务。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `接触式操作` `力觉引导` `模仿学习` `多模态融合` `Transformer` `扩散模型` `机器人操作`

## 📋 核心要点

1. 接触式操作任务需要精确控制交互力，但现有模仿学习方法主要依赖视觉信息，忽略了力觉信息的重要性。
2. ManipForce系统通过手持设备同步采集高频力/扭矩和RGB数据，并提出频率感知多模态Transformer (FMT)进行策略学习。
3. 实验表明，FMT在多个接触式操作任务中显著优于仅使用RGB的基线方法，验证了高频力觉信息和跨模态融合的有效性。

## 📝 摘要（中文）

本文提出ManipForce，一个手持系统，用于在接触式操作的人工示教过程中捕获高频力/扭矩(F/T)和RGB数据。基于这些示教数据，本文引入了频率感知多模态Transformer (FMT)。FMT使用频率和模态感知的嵌入来编码异步RGB和F/T信号，并通过Transformer扩散策略中的双向交叉注意力融合它们。在六个真实世界的接触式操作任务（如齿轮组装、盒子翻转和电池插入）上的大量实验表明，在ManipForce示教数据上训练的FMT实现了稳健的性能，在所有任务中的平均成功率为83%，大大优于仅使用RGB的基线方法。消融实验和采样频率分析进一步证实，结合高频F/T数据和跨模态集成可以提高策略性能，尤其是在需要高精度和稳定接触的任务中。

## 🔬 方法详解

**问题定义**：现有接触式操作任务的模仿学习方法主要依赖视觉信息，忽略了力/扭矩(F/T)信息，导致在需要精确控制交互力的任务中表现不佳。痛点在于无法有效利用接触过程中蕴含的丰富力觉信息，难以实现稳定和精确的操作。

**核心思路**：核心思路是利用手持设备ManipForce采集高质量的RGB和高频F/T数据，并设计频率感知多模态Transformer (FMT)来融合这两种模态的信息。通过频率感知嵌入和跨模态注意力机制，使模型能够更好地理解和利用力觉信息，从而提高策略的性能。

**技术框架**：整体框架包括数据采集和策略学习两个阶段。首先，使用ManipForce手持设备采集人工示教数据，包括RGB图像和高频F/T信号。然后，将这些数据输入到FMT中进行训练。FMT包含频率和模态感知的嵌入层，用于编码RGB和F/T信号，以及双向交叉注意力机制，用于融合不同模态的信息。最后，使用Transformer扩散策略生成动作。

**关键创新**：最重要的技术创新点在于频率感知多模态Transformer (FMT)的设计。FMT能够有效地编码和融合RGB和高频F/T信号，从而更好地利用接触过程中蕴含的力觉信息。与现有方法相比，FMT能够更好地处理异步的多模态数据，并学习到更鲁棒的策略。

**关键设计**：FMT的关键设计包括：1) 频率感知的嵌入层，用于将RGB和F/T信号编码到相同的特征空间；2) 双向交叉注意力机制，用于融合不同模态的信息；3) Transformer扩散策略，用于生成动作。损失函数包括模仿学习损失和扩散模型损失。具体的网络结构参数和训练细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，在六个真实世界的接触式操作任务中，使用ManipForce采集的数据训练的FMT模型取得了显著的性能提升，平均成功率达到83%，大幅超过了仅使用RGB数据的基线方法。消融实验验证了高频F/T数据和跨模态融合对于提高策略性能的重要性。

## 🎯 应用场景

该研究成果可应用于各种需要精确接触控制的机器人操作任务，例如精密装配、医疗手术、以及其他需要在复杂环境中进行稳定操作的场景。通过结合视觉和力觉信息，可以提高机器人的操作精度和鲁棒性，使其能够更好地适应真实世界的复杂环境。

## 📄 摘要（原文）

> Contact-rich manipulation tasks such as precision assembly require precise control of interaction forces, yet existing imitation learning methods rely mainly on vision-only demonstrations. We propose ManipForce, a handheld system designed to capture high-frequency force-torque (F/T) and RGB data during natural human demonstrations for contact-rich manipulation. Building on these demonstrations, we introduce the Frequency-Aware Multimodal Transformer (FMT). FMT encodes asynchronous RGB and F/T signals using frequency- and modality-aware embeddings and fuses them via bi-directional cross-attention within a transformer diffusion policy. Through extensive experiments on six real-world contact-rich manipulation tasks - such as gear assembly, box flipping, and battery insertion - FMT trained on ManipForce demonstrations achieves robust performance with an average success rate of 83% across all tasks, substantially outperforming RGB-only baselines. Ablation and sampling-frequency analyses further confirm that incorporating high-frequency F/T data and cross-modal integration improves policy performance, especially in tasks demanding high precision and stable contact.

