---
layout: default
title: ARMADA: Autonomous Online Failure Detection and Human Shared Control Empower Scalable Real-world Deployment and Adaptation
---

# ARMADA: Autonomous Online Failure Detection and Human Shared Control Empower Scalable Real-world Deployment and Adaptation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.02298" target="_blank" class="toolbar-btn">arXiv: 2510.02298v1</a>
    <a href="https://arxiv.org/pdf/2510.02298.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02298v1" 
            onclick="toggleFavorite(this, '2510.02298v1', 'ARMADA: Autonomous Online Failure Detection and Human Shared Control Empower Scalable Real-world Deployment and Adaptation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Wenye Yu, Jun Lv, Zixi Ying, Yang Jin, Chuan Wen, Cewu Lu

**分类**: cs.RO

**发布日期**: 2025-10-02

---

## 💡 一句话要点

**ARMADA：结合自主故障检测与人机共享控制，实现机器人部署与自适应的扩展**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人机协作` `模仿学习` `故障检测` `机器人部署` `自主学习`

## 📋 核心要点

1. 现有模仿学习方法在真实场景中部署时，面临领域数据不足和人工标注成本高昂的问题。
2. ARMADA系统通过FLOAT自主在线故障检测，减少对人工监督的依赖，实现高效的领域内数据获取。
3. 实验表明，ARMADA在多个真实任务中显著提升了成功率，并降低了人工干预率。

## 📝 摘要（中文）

模仿学习在从大规模真实世界数据集学习方面展现了潜力。然而，预训练策略通常在缺乏足够的领域内数据时表现不佳。此外，人工收集的演示数据需要大量劳动，并且往往包含混合质量的数据和冗余信息。作为一种解决方案，人机回路系统收集特定领域的数据用于策略后训练，并利用闭环策略反馈来提供信息丰富的指导，但通常需要在策略部署期间进行全职人工监控。在这项工作中，我们设计了ARMADA，一个具有人机回路共享控制的多机器人部署和自适应系统，其特点是一种名为FLOAT的自主在线故障检测方法。借助FLOAT，ARMADA能够并行策略部署，并且仅在必要时请求人工干预，从而显著减少对人工监督的依赖。因此，ARMADA能够高效获取领域内数据，并实现更具扩展性的部署和更快地适应新场景。我们在四个真实世界的任务上评估了ARMADA的性能。FLOAT平均达到近95%的准确率，超过了先前最先进的故障检测方法20%以上。此外，与先前的人机回路学习方法相比，经过多轮策略部署和后训练，ARMADA的成功率提高了4倍以上，人工干预率降低了2倍以上。

## 🔬 方法详解

**问题定义**：论文旨在解决模仿学习策略在真实世界机器人部署中，因领域数据不足和人工干预成本过高而导致的性能瓶颈问题。现有方法通常需要大量人工标注数据或全时人工监控，限制了策略的扩展性和适应性。

**核心思路**：论文的核心思路是利用自主在线故障检测方法（FLOAT）来减少对人工监督的依赖，从而实现更高效的领域内数据获取和策略自适应。通过FLOAT，系统可以在策略执行过程中自动检测到潜在的失败情况，并仅在必要时请求人工干预。

**技术框架**：ARMADA系统包含以下主要模块：1) 预训练的模仿学习策略；2) FLOAT自主在线故障检测模块；3) 人机共享控制接口；4) 策略后训练模块。系统首先使用预训练策略进行部署，FLOAT模块实时监测策略执行情况，当检测到潜在失败时，系统请求人工干预。人工干预数据用于策略后训练，提升策略性能。

**关键创新**：论文最重要的技术创新点是FLOAT自主在线故障检测方法。FLOAT能够准确地识别策略执行过程中的潜在失败情况，从而减少对人工监督的依赖。与现有故障检测方法相比，FLOAT具有更高的准确率和更低的误报率。

**关键设计**：关于FLOAT的具体设计细节，论文中没有详细展开。但可以推测，FLOAT可能利用了策略执行过程中的传感器数据、状态信息等，通过机器学习模型（例如分类器或异常检测器）来判断当前状态是否可能导致失败。损失函数的设计目标是最大化故障检测的准确率，同时最小化误报率。具体的网络结构和参数设置未知。

## 📊 实验亮点

实验结果表明，FLOAT故障检测的平均准确率达到近95%，超过了现有技术水平20%以上。与传统人机回路学习方法相比，ARMADA系统在多轮策略部署和后训练后，成功率提高了4倍以上，人工干预率降低了2倍以上，验证了该方法的有效性。

## 🎯 应用场景

该研究成果可广泛应用于各种需要机器人自主操作的场景，例如物流、仓储、家庭服务、农业等。通过减少对人工监督的依赖，可以显著降低运营成本，提高工作效率，并使机器人能够更快地适应新的环境和任务。

## 📄 摘要（原文）

> Imitation learning has shown promise in learning from large-scale real-world datasets. However, pretrained policies usually perform poorly without sufficient in-domain data. Besides, human-collected demonstrations entail substantial labour and tend to encompass mixed-quality data and redundant information. As a workaround, human-in-the-loop systems gather domain-specific data for policy post-training, and exploit closed-loop policy feedback to offer informative guidance, but usually require full-time human surveillance during policy rollout. In this work, we devise ARMADA, a multi-robot deployment and adaptation system with human-in-the-loop shared control, featuring an autonomous online failure detection method named FLOAT. Thanks to FLOAT, ARMADA enables paralleled policy rollout and requests human intervention only when necessary, significantly reducing reliance on human supervision. Hence, ARMADA enables efficient acquisition of in-domain data, and leads to more scalable deployment and faster adaptation to new scenarios. We evaluate the performance of ARMADA on four real-world tasks. FLOAT achieves nearly 95% accuracy on average, surpassing prior state-of-the-art failure detection approaches by over 20%. Besides, ARMADA manifests more than 4$\times$ increase in success rate and greater than 2$\times$ reduction in human intervention rate over multiple rounds of policy rollout and post-training, compared to previous human-in-the-loop learning methods.

