---
layout: default
title: "InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency"
---

# InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18265" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18265v2</a>
  <a href="https://arxiv.org/pdf/2508.18265.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18265v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18265v2', 'InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiyun Wang, Zhangwei Gao, Lixin Gu, Hengjun Pu, Long Cui, Xingguang Wei, Zhaoyang Liu, Linglin Jing, Shenglong Ye, Jie Shao, Zhaokai Wang, Zhe Chen, Hongjie Zhang, Ganlin Yang, Haomin Wang, Qi Wei, Jinhui Yin, Wenhao Li, Erfei Cui, Guanzhou Chen, Zichen Ding, Changyao Tian, Zhenyu Wu, Jingjing Xie, Zehao Li, Bowen Yang, Yuchen Duan, Xuehui Wang, Zhi Hou, Haoran Hao, Tianyi Zhang, Songze Li, Xiangyu Zhao, Haodong Duan, Nianchen Deng, Bin Fu, Yinan He, Yi Wang, Conghui He, Botian Shi, Junjun He, Yingtong Xiong, Han Lv, Lijun Wu, Wenqi Shao, Kaipeng Zhang, Huipeng Deng, Biqing Qi, Jiaye Ge, Qipeng Guo, Wenwei Zhang, Songyang Zhang, Maosong Cao, Junyao Lin, Kexian Tang, Jianfei Gao, Haian Huang, Yuzhe Gu, Chengqi Lyu, Huanze Tang, Rui Wang, Haijun Lv, Wanli Ouyang, Limin Wang, Min Dou, Xizhou Zhu, Tong Lu, Dahua Lin, Jifeng Dai, Weijie Su, Bowen Zhou, Kai Chen, Yu Qiao, Wenhai Wang, Gen Luo

**分类**: cs.CV

**发布日期**: 2025-08-25 (更新: 2025-08-27)

---

## 💡 一句话要点

**提出InternVL3.5以提升多模态模型的推理能力与效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `推理能力` `级联强化学习` `视觉分辨率路由器` `解耦部署` `开源模型` `计算效率` `智能交互`

## 📋 核心要点

1. 现有多模态模型在推理能力和效率上存在不足，难以满足复杂任务的需求。
2. 论文提出级联强化学习框架和视觉分辨率路由器，以提升推理能力和推理效率。
3. 实验结果显示，InternVL3.5在推理性能上提升16.0%，推理速度提升4.05倍，表现优异。

## 📝 摘要（中文）

我们介绍了InternVL3.5，这是一系列开源多模态模型，显著提升了多样性、推理能力和推理效率。关键创新是级联强化学习（Cascade RL）框架，通过离线和在线强化学习的两阶段过程增强推理能力。这种粗到细的训练策略在下游推理任务（如MMMU和MathVista）上取得了显著改进。为优化效率，我们提出了视觉分辨率路由器（ViR），动态调整视觉标记的分辨率而不影响性能。结合ViR，我们的解耦视觉-语言部署（DvD）策略将视觉编码器和语言模型分布在不同的GPU上，有效平衡计算负载。这些贡献使InternVL3.5在推理性能上提升了16.0%，并实现了4.05倍的推理速度提升。此外，InternVL3.5支持GUI交互和具身智能等新能力。我们的最大模型InternVL3.5-241B-A28B在开放源代码的多模态、推理、文本和代理任务中取得了领先的结果，缩小了与商业模型（如GPT-5）的性能差距。所有模型和代码均已公开发布。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态模型在推理能力和效率方面的不足，尤其是在复杂推理任务中的表现不佳。现有方法往往无法有效平衡推理精度与计算效率。

**核心思路**：论文的核心思路是通过级联强化学习框架提升推理能力，采用离线和在线强化学习的两阶段训练策略，以实现稳定收敛和精细对齐。

**技术框架**：整体架构包括两个主要模块：级联强化学习框架和视觉分辨率路由器。级联强化学习分为离线和在线两个阶段，视觉分辨率路由器则动态调整视觉标记的分辨率。

**关键创新**：最重要的技术创新是级联强化学习框架的引入，这一设计使得模型在推理任务中表现出更高的灵活性和准确性，与现有方法相比具有显著的优势。

**关键设计**：在模型设计中，采用了动态调整视觉标记分辨率的策略，并通过解耦视觉编码器和语言模型的方式来优化计算资源的使用，确保在不同GPU上高效运行。具体的损失函数和参数设置在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，InternVL3.5在推理性能上提升了16.0%，并实现了4.05倍的推理速度提升，相较于前一版本InternVL3，表现显著优异。此外，模型在多模态、推理、文本和代理任务中均取得了领先的结果，缩小了与商业模型的性能差距。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化客服、教育辅导等多模态交互场景。通过提升推理能力和效率，InternVL3.5能够更好地理解和处理复杂的用户请求，提供更为精准的反馈和服务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce InternVL 3.5, a new family of open-source multimodal models that significantly advances versatility, reasoning capability, and inference efficiency along the InternVL series. A key innovation is the Cascade Reinforcement Learning (Cascade RL) framework, which enhances reasoning through a two-stage process: offline RL for stable convergence and online RL for refined alignment. This coarse-to-fine training strategy leads to substantial improvements on downstream reasoning tasks, e.g., MMMU and MathVista. To optimize efficiency, we propose a Visual Resolution Router (ViR) that dynamically adjusts the resolution of visual tokens without compromising performance. Coupled with ViR, our Decoupled Vision-Language Deployment (DvD) strategy separates the vision encoder and language model across different GPUs, effectively balancing computational load. These contributions collectively enable InternVL3.5 to achieve up to a +16.0\% gain in overall reasoning performance and a 4.05$\times$ inference speedup compared to its predecessor, i.e., InternVL3. In addition, InternVL3.5 supports novel capabilities such as GUI interaction and embodied agency. Notably, our largest model, i.e., InternVL3.5-241B-A28B, attains state-of-the-art results among open-source MLLMs across general multimodal, reasoning, text, and agentic tasks -- narrowing the performance gap with leading commercial models like GPT-5. All models and code are publicly released.

