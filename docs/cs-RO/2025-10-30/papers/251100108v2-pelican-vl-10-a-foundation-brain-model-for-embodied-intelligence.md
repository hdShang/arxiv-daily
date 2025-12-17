---
layout: default
title: Pelican-VL 1.0: A Foundation Brain Model for Embodied Intelligence
---

# Pelican-VL 1.0: A Foundation Brain Model for Embodied Intelligence

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00108" target="_blank" class="toolbar-btn">arXiv: 2511.00108v2</a>
    <a href="https://arxiv.org/pdf/2511.00108.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00108v2" 
            onclick="toggleFavorite(this, '2511.00108v2', 'Pelican-VL 1.0: A Foundation Brain Model for Embodied Intelligence')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yi Zhang, Che Liu, Xiancong Ren, Hanchu Ni, Shuai Zhang, Zeyuan Ding, Jiayu Hu, Hanzhe Shan, Zhenwei Niu, Zhaoyang Liu, Shuang Liu, Yue Zhao, Junbo Qi, Qinfan Zhang, Dengjie Li, Yidong Wang, Jiachen Luo, Yong Dai, Zenglin Xu, Bin Shen, Qifan Wang, Jian Tang, Xiaozhu Ju

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-10-30 (更新: 2025-11-14)

---

## 💡 一句话要点

**Pelican-VL 1.0：用于具身智能的开源基础大脑模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `多模态学习` `强化学习` `数据提炼` `大脑模型`

## 📋 核心要点

1. 现有具身智能模型在数据质量和训练效率方面存在瓶颈，难以充分利用大规模数据。
2. Pelican-VL 1.0 通过 metaloop 提炼高质量数据集，并采用 DPPO 框架进行刻意练习，提升模型性能。
3. 实验表明，Pelican-VL 1.0 性能优于同等规模的开源模型，并与领先的专有系统在具身基准测试中表现相当。

## 📝 摘要（中文）

本报告介绍了Pelican-VL 1.0，这是一个新的开源具身大脑模型系列，参数规模从70亿到720亿不等。我们的明确目标是：将强大的智能嵌入到各种具身环境中。Pelican-VL 1.0是目前最大规模的开源具身多模态大脑模型。其核心优势在于数据能力和智能自适应学习机制的深度整合。具体来说，metaloop从包含40亿+ tokens 的原始数据集中提炼出了高质量的数据集。Pelican-VL 1.0 在一个包含 1000+ A800 GPU 的大型集群上进行训练，每个 checkpoint 消耗超过 50k+ A800 GPU-hours。这使得其性能比基础模型提升了 20.3%，并且比 100B 级别的开源模型高出 10.6%，在著名的具身基准测试中与领先的专有系统相当。我们建立了一个受人类元认知启发的全新框架 DPPO (Deliberate Practice Policy Optimization)，用于训练 Pelican-VL 1.0。我们将其操作化为一个 metaloop，教导 AI 进行刻意练习，这是一个 RL-Refine-Diagnose-SFT 循环。

## 🔬 方法详解

**问题定义**：现有具身智能模型面临数据质量不高、训练效率低下等问题，限制了模型在复杂具身任务中的表现。现有方法难以有效利用大规模原始数据，并且缺乏有效的自适应学习机制，导致模型泛化能力不足。

**核心思路**：Pelican-VL 1.0 的核心思路是通过数据提炼和强化学习优化相结合，提升模型在具身环境中的智能水平。通过 metaloop 提炼高质量数据集，减少噪声数据的影响；通过 DPPO 框架模拟人类的刻意练习过程，使模型能够自适应地学习和改进。

**技术框架**：Pelican-VL 1.0 的训练框架主要包含以下几个阶段：1) 数据收集：收集包含大量 tokens 的原始数据集。2) 数据提炼：使用 metaloop 从原始数据集中提炼高质量的数据集。3) 模型训练：使用提炼后的数据集训练基础模型。4) 策略优化：使用 DPPO 框架对模型进行强化学习优化，使其能够更好地适应具身环境。DPPO 框架包含 RL (Reinforcement Learning)、Refine、Diagnose 和 SFT (Supervised Fine-Tuning) 四个阶段。

**关键创新**：Pelican-VL 1.0 的关键创新在于 DPPO 框架和 metaloop 数据提炼方法。DPPO 框架模拟人类的刻意练习过程，使模型能够自适应地学习和改进。metaloop 数据提炼方法能够从大规模原始数据集中提取高质量的数据，减少噪声数据的影响。与现有方法相比，DPPO 框架更加注重模型的自适应学习能力，而 metaloop 数据提炼方法能够更有效地利用大规模数据。

**关键设计**：DPPO 框架中的奖励函数设计是关键。奖励函数需要能够准确地反映模型在具身环境中的表现，并且能够引导模型朝着正确的方向学习。metaloop 数据提炼方法中的提炼策略也是关键。提炼策略需要能够有效地识别和提取高质量的数据，同时过滤掉噪声数据。具体的参数设置和网络结构细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

Pelican-VL 1.0 在具身基准测试中表现出色，比基础模型提升了 20.3%，并且比 100B 级别的开源模型高出 10.6%，与领先的专有系统相当。这表明 Pelican-VL 1.0 在具身智能领域具有很强的竞争力，并且具有很大的应用潜力。

## 🎯 应用场景

Pelican-VL 1.0 可应用于机器人控制、自动驾驶、虚拟现实等领域。通过将强大的智能嵌入到各种具身环境中，可以实现更智能、更自主的机器人系统。例如，可以用于开发能够自主完成复杂任务的机器人助手，或者用于开发更安全、更可靠的自动驾驶系统。该研究的未来影响在于推动具身智能技术的发展，实现更智能、更人性化的机器人系统。

## 📄 摘要（原文）

> This report presents Pelican-VL 1.0, a new family of open-source embodied brain models with parameter scales ranging from 7 billion to 72 billion. Our explicit mission is clearly stated as: To embed powerful intelligence into various embodiments. Pelican-VL 1.0 is currently the largest-scale open-source embodied multimodal brain model. Its core advantage lies in the in-depth integration of data power and intelligent adaptive learning mechanisms. Specifically, metaloop distilled a high-quality dataset from a raw dataset containing 4+ billion tokens. Pelican-VL 1.0 is trained on a large-scale cluster of 1000+ A800 GPUs, consuming over 50k+ A800 GPU-hours per checkpoint. This translates to a 20.3% performance uplift from its base model and outperforms 100B-level open-source counterparts by 10.6%, placing it on par with leading proprietary systems on well-known embodied benchmarks. We establish a novel framework, DPPO (Deliberate Practice Policy Optimization), inspired by human metacognition to train Pelican-VL 1.0. We operationalize this as a metaloop that teaches the AI to practice deliberately, which is a RL-Refine-Diagnose-SFT loop.

