---
layout: default
title: "FiLM-Nav: Efficient and Generalizable Navigation via VLM Fine-tuning"
---

# FiLM-Nav: Efficient and Generalizable Navigation via VLM Fine-tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16445" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16445v1</a>
  <a href="https://arxiv.org/pdf/2509.16445.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16445v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16445v1', 'FiLM-Nav: Efficient and Generalizable Navigation via VLM Fine-tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Naoki Yokoyama, Sehoon Ha

**分类**: cs.RO

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**FiLM-Nav：通过VLM微调实现高效且泛化的导航**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `具身导航` `迁移学习` `强化学习` `机器人` `语义理解` `开放词汇` `微调`

## 📋 核心要点

1. 现有方法难以将视觉-语言模型(VLM)的强大语义理解能力有效应用于具身决策，尤其是在复杂环境导航中。
2. FiLM-Nav直接微调预训练VLM作为导航策略，通过视觉轨迹和导航目标学习选择最佳探索前沿。
3. 在ObjectNav、OVON等任务混合数据集上微调，FiLM-Nav在HM3D数据集上取得了显著的性能提升，展示了强大的泛化能力。

## 📝 摘要（中文）

本文提出FiLM-Nav，一种直接微调预训练视觉-语言模型(VLM)作为导航策略的方法，旨在使机器人助手能够在复杂环境中导航并定位自由文本描述的物体。与主要以零样本方式或用于地图标注的方法不同，FiLM-Nav通过直接调节原始视觉轨迹历史和导航目标来学习选择最佳探索前沿。利用有针对性的模拟具身经验，VLM能够将其强大的预训练表示与目标驱动导航相关的特定动态和视觉模式相结合。关键在于，结合ObjectNav、OVON、ImageNav和辅助空间推理任务的多元数据混合进行微调，对于实现鲁棒性和广泛的泛化至关重要。FiLM-Nav在开放词汇方法中，于HM3D ObjectNav上实现了SPL和成功率的新SOTA，并在具有挑战性的HM3D-OVON基准测试中实现了SOTA SPL，展示了对未见过的物体类别的强大泛化能力。这项工作验证了在多样化的模拟具身数据上直接微调VLM是实现可泛化和高效的语义导航能力的一种非常有效的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人如何在复杂环境中，根据自由文本描述的目标，进行高效且泛化的导航问题。现有方法通常依赖于零样本迁移或将VLM用于地图标注，无法充分利用VLM的语义理解能力，且泛化性不足。

**核心思路**：论文的核心思路是直接将预训练的VLM微调为导航策略。通过在模拟环境中进行有针对性的具身学习，使VLM能够将预训练的知识与导航任务中的视觉模式和环境动态相结合，从而实现更高效和泛化的导航。

**技术框架**：FiLM-Nav的整体框架包括以下几个主要部分：1) 视觉输入模块，用于处理来自机器人的视觉轨迹历史；2) 语言输入模块，用于处理导航目标的文本描述；3) VLM，作为核心决策模块，接收视觉和语言输入，并输出下一步的导航动作；4) 训练模块，通过在模拟环境中进行强化学习或监督学习，微调VLM的参数。

**关键创新**：最重要的技术创新点在于直接将VLM作为导航策略进行微调。与传统方法相比，FiLM-Nav能够更充分地利用VLM的语义理解能力，并将其与导航任务的特定需求相结合。此外，通过在多样化的数据集上进行微调，FiLM-Nav能够实现更强的泛化能力。

**关键设计**：论文的关键设计包括：1) 使用Transformer架构的VLM作为导航策略；2) 设计合适的视觉和语言输入表示，以便VLM能够有效地处理这些信息；3) 使用多样化的数据集进行微调，包括ObjectNav、OVON、ImageNav和辅助空间推理任务；4) 采用合适的损失函数和优化算法，以有效地训练VLM。

## 📊 实验亮点

FiLM-Nav在HM3D ObjectNav任务上，相较于开放词汇方法，取得了SPL和成功率的新SOTA。在更具挑战性的HM3D-OVON基准测试中，FiLM-Nav也实现了SOTA SPL，证明了其在未见过的物体类别上的强大泛化能力。这些实验结果表明，直接微调VLM是一种有效的语义导航方法。

## 🎯 应用场景

FiLM-Nav技术可应用于家庭服务机器人、仓储物流机器人、自动驾驶等领域。例如，家庭服务机器人可以根据用户的语音指令，在室内环境中找到指定的物品。该研究的实际价值在于提升了机器人的自主导航能力和环境适应性，未来有望实现更智能、更高效的机器人服务。

## 📄 摘要（原文）

> Enabling robotic assistants to navigate complex environments and locate objects described in free-form language is a critical capability for real-world deployment. While foundation models, particularly Vision-Language Models (VLMs), offer powerful semantic understanding, effectively adapting their web-scale knowledge for embodied decision-making remains a key challenge. We present FiLM-Nav (Fine-tuned Language Model for Navigation), an approach that directly fine-tunes pre-trained VLM as the navigation policy. In contrast to methods that use foundation models primarily in a zero-shot manner or for map annotation, FiLM-Nav learns to select the next best exploration frontier by conditioning directly on raw visual trajectory history and the navigation goal. Leveraging targeted simulated embodied experience allows the VLM to ground its powerful pre-trained representations in the specific dynamics and visual patterns relevant to goal-driven navigation. Critically, fine-tuning on a diverse data mixture combining ObjectNav, OVON, ImageNav, and an auxiliary spatial reasoning task proves essential for achieving robustness and broad generalization. FiLM-Nav sets a new state-of-the-art in both SPL and success rate on HM3D ObjectNav among open-vocabulary methods, and sets a state-of-the-art SPL on the challenging HM3D-OVON benchmark, demonstrating strong generalization to unseen object categories. Our work validates that directly fine-tuning VLMs on diverse simulated embodied data is a highly effective pathway towards generalizable and efficient semantic navigation capabilities.

