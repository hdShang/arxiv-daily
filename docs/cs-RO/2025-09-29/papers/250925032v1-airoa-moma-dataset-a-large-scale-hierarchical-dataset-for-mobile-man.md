---
layout: default
title: "AIRoA MoMa Dataset: A Large-Scale Hierarchical Dataset for Mobile Manipulation"
---

# AIRoA MoMa Dataset: A Large-Scale Hierarchical Dataset for Mobile Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25032" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25032v1</a>
  <a href="https://arxiv.org/pdf/2509.25032.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25032v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25032v1', 'AIRoA MoMa Dataset: A Large-Scale Hierarchical Dataset for Mobile Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ryosuke Takanami, Petr Khrapchenkov, Shu Morikuni, Jumpei Arima, Yuta Takaba, Shunsuke Maeda, Takuya Okubo, Genki Sano, Satoshi Sekioka, Aoi Kadoya, Motonari Kambara, Naoya Nishiura, Haruto Suzuki, Takanori Yoshimoto, Koya Sakamoto, Shinnosuke Ono, Hu Yang, Daichi Yashima, Aoi Horo, Tomohiro Motoda, Kensuke Chiyoma, Hiroshi Ito, Koki Fukuda, Akihito Goto, Kazumi Morinaga, Yuya Ikeda, Riko Kawada, Masaki Yoshikawa, Norio Kosuge, Yuki Noguchi, Kei Ota, Tatsuya Matsushima, Yusuke Iwasawa, Yutaka Matsuo, Tetsuya Ogata

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-09-29

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/airoa-org)

---

## 💡 一句话要点

**AIRoA MoMa：用于移动操作的大规模分层数据集，助力通用机器人**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `移动操作` `机器人数据集` `多模态学习` `分层学习` `力/扭矩传感` `视觉-语言-动作模型` `机器人学习` `长时程任务`

## 📋 核心要点

1. 现有移动操作数据集缺乏同步力/扭矩传感、分层注释和失败案例，限制了通用机器人的发展。
2. AIRoA MoMa数据集通过提供大规模、多模态数据，以及分层注释，弥补了现有数据集的不足。
3. 该数据集包含25469个episode，使用HSR机器人收集，并标准化为LeRobot v2.1格式，为研究提供基准。

## 📝 摘要（中文）

本文介绍了AIRoA MoMa数据集，这是一个用于移动操作的大规模真实世界多模态数据集。随着机器人从受控环境过渡到非结构化的人类环境，构建能够可靠地遵循自然语言指令的通用智能体仍然是一个核心挑战。为了促进在鲁棒的移动操作方面的进展，需要捕获富含接触和长时程任务的大规模多模态数据集，然而现有的资源缺乏同步的力/扭矩传感、分层注释和显式的失败案例。AIRoA MoMa数据集通过集成同步的RGB图像、关节状态、六轴腕部力/扭矩信号和内部机器人状态，以及用于分层学习和错误分析的子目标和原始动作的新型两层注释模式，来解决这一差距。初始数据集包含使用Human Support Robot (HSR)收集的25469个episode（约94小时），并完全标准化为LeRobot v2.1格式。通过独特地集成移动操作、富含接触的交互和长时程结构，AIRoA MoMa为推进下一代视觉-语言-动作模型提供了一个关键的基准。数据集的第一个版本现已在https://huggingface.co/datasets/airoa-org/airoa-moma 上提供。

## 🔬 方法详解

**问题定义**：现有移动操作数据集在以下几个方面存在不足：缺乏同步的力/扭矩传感数据，难以进行接触力控制和分析；缺乏分层注释，难以进行分层学习和任务分解；缺乏显式的失败案例，难以进行鲁棒性学习和错误分析。这些不足限制了通用机器人在复杂、非结构化环境中执行任务的能力。

**核心思路**：AIRoA MoMa数据集的核心思路是提供一个大规模、多模态、分层注释的数据集，以促进移动操作领域的研究。通过同步采集RGB图像、关节状态、力/扭矩信号和内部机器人状态，数据集能够支持多种模态信息的融合学习。通过两层注释模式（子目标和原始动作），数据集能够支持分层学习和任务分解。通过包含失败案例，数据集能够支持鲁棒性学习和错误分析。

**技术框架**：AIRoA MoMa数据集的整体框架包括数据采集、数据标注和数据发布三个主要阶段。数据采集阶段使用Human Support Robot (HSR)在真实环境中执行各种移动操作任务，并同步采集多种模态的数据。数据标注阶段采用两层注释模式，对每个episode进行子目标和原始动作的标注。数据发布阶段将数据集标准化为LeRobot v2.1格式，并在Hugging Face上发布。

**关键创新**：AIRoA MoMa数据集的关键创新在于其大规模、多模态和分层注释的特性。与现有数据集相比，AIRoA MoMa数据集规模更大，包含更多模态的信息，并且提供了更细粒度的分层注释。此外，AIRoA MoMa数据集还包含了显式的失败案例，这对于鲁棒性学习至关重要。

**关键设计**：AIRoA MoMa数据集的关键设计包括：1) 使用HSR机器人进行数据采集，保证了数据的真实性和多样性；2) 采用同步采集多种模态数据的方式，方便进行多模态信息的融合学习；3) 采用两层注释模式，方便进行分层学习和任务分解；4) 包含显式的失败案例，方便进行鲁棒性学习和错误分析；5) 将数据集标准化为LeRobot v2.1格式，方便研究人员使用。

## 📊 实验亮点

AIRoA MoMa数据集包含25469个episode，总时长约94小时，是目前最大的移动操作数据集之一。该数据集提供了同步的RGB图像、关节状态、六轴腕部力/扭矩信号和内部机器人状态，以及用于分层学习和错误分析的子目标和原始动作的新型两层注释模式。该数据集为下一代视觉-语言-动作模型提供了一个关键的基准。

## 🎯 应用场景

AIRoA MoMa数据集可广泛应用于机器人移动操作领域，例如视觉-语言导航、操作技能学习、机器人故障诊断等。该数据集能够促进通用机器人的发展，使其能够在复杂、非结构化的环境中执行各种任务，例如家庭服务、医疗辅助、工业自动化等。未来，基于该数据集的研究有望提升机器人的智能化水平，使其更好地服务于人类。

## 📄 摘要（原文）

> As robots transition from controlled settings to unstructured human environments, building generalist agents that can reliably follow natural language instructions remains a central challenge. Progress in robust mobile manipulation requires large-scale multimodal datasets that capture contact-rich and long-horizon tasks, yet existing resources lack synchronized force-torque sensing, hierarchical annotations, and explicit failure cases. We address this gap with the AIRoA MoMa Dataset, a large-scale real-world multimodal dataset for mobile manipulation. It includes synchronized RGB images, joint states, six-axis wrist force-torque signals, and internal robot states, together with a novel two-layer annotation schema of sub-goals and primitive actions for hierarchical learning and error analysis. The initial dataset comprises 25,469 episodes (approx. 94 hours) collected with the Human Support Robot (HSR) and is fully standardized in the LeRobot v2.1 format. By uniquely integrating mobile manipulation, contact-rich interaction, and long-horizon structure, AIRoA MoMa provides a critical benchmark for advancing the next generation of Vision-Language-Action models. The first version of our dataset is now available at https://huggingface.co/datasets/airoa-org/airoa-moma .

