---
layout: default
title: "UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning"
---

# UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02544" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02544v2</a>
  <a href="https://arxiv.org/pdf/2509.02544.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02544v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02544v2', 'UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoming Wang, Haoyang Zou, Huatong Song, Jiazhan Feng, Junjie Fang, Junting Lu, Longxiang Liu, Qinyu Luo, Shihao Liang, Shijue Huang, Wanjun Zhong, Yining Ye, Yujia Qin, Yuwen Xiong, Yuxin Song, Zhiyong Wu, Aoyan Li, Bo Li, Chen Dun, Chong Liu, Daoguang Zan, Fuxing Leng, Hanbin Wang, Hao Yu, Haobin Chen, Hongyi Guo, Jing Su, Jingjia Huang, Kai Shen, Kaiyu Shi, Lin Yan, Peiyao Zhao, Pengfei Liu, Qinghao Ye, Renjie Zheng, Shulin Xin, Wayne Xin Zhao, Wen Heng, Wenhao Huang, Wenqian Wang, Xiaobo Qin, Yi Lin, Youbin Wu, Zehui Chen, Zihao Wang, Baoquan Zhong, Xinchun Zhang, Xujing Li, Yuanfan Li, Zhongkai Zhao, Chengquan Jiang, Faming Wu, Haotian Zhou, Jinlin Pang, Li Han, Qi Liu, Qianli Ma, Siyao Liu, Songhua Cai, Wenqi Fu, Xin Liu, Yaohui Wang, Zhi Zhang, Bo Zhou, Guoliang Li, Jiajun Shi, Jiale Yang, Jie Tang, Li Li, Qihua Han, Taoran Lu, Woyu Lin, Xiaokang Tong, Xinyao Li, Yichi Zhang, Yu Miao, Zhengxuan Jiang, Zili Li, Ziyuan Zhao, Chenxin Li, Dehua Ma, Feng Lin, Ge Zhang, Haihua Yang, Hangyu Guo, Hongda Zhu, Jiaheng Liu, Junda Du, Kai Cai, Kuanye Li, Lichen Yuan, Meilan Han, Minchao Wang, Shuyue Guo, Tianhao Cheng, Xiaobo Ma, Xiaojun Xiao, Xiaolong Huang, Xinjie Chen, Yidi Du, Yilin Chen, Yiwen Wang, Zhaojian Li, Zhenzhu Yang, Zhiyuan Zeng, Chaolin Jin, Chen Li, Hao Chen, Haoli Chen, Jian Chen, Qinghao Zhao, Guang Shi

**分类**: cs.AI, cs.CL, cs.CV, cs.HC

**发布日期**: 2025-09-02 (更新: 2025-09-05)

---

## 💡 一句话要点

**UI-TARS-2：通过多轮强化学习提升GUI智能体性能，实现更强的泛化能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `GUI智能体` `强化学习` `多轮交互` `数据飞轮` `环境模拟`

## 📋 核心要点

1. 现有GUI智能体模型在数据可扩展性、多轮强化学习的稳定性、仅依赖GUI操作的局限性以及环境稳定性方面存在挑战。
2. UI-TARS-2通过数据飞轮、稳定的多轮强化学习框架、混合GUI环境和统一沙箱平台，系统性地解决了上述挑战。
3. 实验表明，UI-TARS-2在多个GUI和游戏基准测试中显著优于现有模型，并能泛化到长时程信息搜索和软件工程任务。

## 📝 摘要（中文）

本文介绍了UI-TARS-2，一种以GUI为中心的智能体模型，旨在解决GUI自主智能体开发中的挑战。该模型通过系统性的训练方法，包括可扩展的数据生成的数据飞轮、稳定的多轮强化学习框架、集成文件系统和终端的混合GUI环境以及用于大规模rollout的统一沙箱平台，从而克服了数据可扩展性、多轮强化学习、GUI操作限制和环境稳定性等问题。实验结果表明，UI-TARS-2在GUI基准测试（Online-Mind2Web、OSWorld、WindowsAgentArena和AndroidWorld）上显著优于其前身UI-TARS-1.5以及Claude和OpenAI等强基线模型。在游戏环境中，它在15个游戏的套件中获得了59.8的平均归一化分数，与前沿专有模型（如OpenAI o3）在LMGame-Bench上具有竞争力。此外，该模型可以推广到长时程信息搜索任务和软件工程基准，突显了其在各种智能体任务中的鲁棒性。对训练动态的详细分析进一步提供了关于在大规模智能体强化学习中实现稳定性和效率的见解。这些结果强调了UI-TARS-2在推进GUI智能体状态方面的潜力，并展示了对真实世界交互场景的强大泛化能力。

## 🔬 方法详解

**问题定义**：现有GUI智能体模型面临数据规模有限、多轮交互训练不稳定、仅依赖GUI操作导致能力受限、以及环境不稳定等问题。这些问题限制了智能体在复杂真实场景中的应用，例如长时程任务和软件工程任务。现有方法难以有效解决这些问题，导致智能体性能提升受阻。

**核心思路**：UI-TARS-2的核心思路是通过系统性的训练方法，解决数据、训练和环境方面的挑战。具体来说，利用数据飞轮实现可扩展的数据生成，稳定多轮强化学习框架，构建混合GUI环境，并使用统一沙箱平台进行大规模rollout。这种多管齐下的方法旨在提升智能体的泛化能力和鲁棒性。

**技术框架**：UI-TARS-2的技术框架包含以下几个主要模块：1) **数据飞轮**：用于生成大规模训练数据，解决数据稀缺问题。2) **多轮强化学习框架**：采用稳定化的训练策略，提升训练过程的稳定性。3) **混合GUI环境**：集成文件系统和终端，扩展智能体的操作能力。4) **统一沙箱平台**：提供安全可靠的rollout环境，支持大规模实验。整体流程是从数据飞轮生成数据，然后使用多轮强化学习框架训练智能体，并在混合GUI环境和沙箱平台中进行评估和部署。

**关键创新**：UI-TARS-2的关键创新在于其系统性的训练方法，它不仅仅关注模型本身，而是从数据、训练和环境三个维度同时进行优化。这种综合性的方法使得UI-TARS-2能够有效地解决现有GUI智能体模型面临的挑战，并取得显著的性能提升。与现有方法相比，UI-TARS-2更加注重环境的模拟和数据的生成，从而提升了智能体的泛化能力。

**关键设计**：论文中没有详细说明关键的参数设置、损失函数、网络结构等技术细节。这些细节可能属于专有信息，或者在后续的论文中进行更详细的描述。但是，可以推测，在多轮强化学习框架中，可能采用了例如经验回放、目标网络等技术来稳定训练过程。在混合GUI环境中，需要设计合适的接口来连接GUI、文件系统和终端，并定义相应的操作空间。

## 📊 实验亮点

UI-TARS-2在多个GUI基准测试中取得了显著的性能提升，例如在Online-Mind2Web上达到88.2，在OSWorld上达到47.5，在WindowsAgentArena上达到50.6，在AndroidWorld上达到73.3，超越了Claude和OpenAI等强基线模型。在游戏环境中，它在15个游戏的套件中获得了59.8的平均归一化分数，与OpenAI o3等前沿专有模型在LMGame-Bench上具有竞争力。

## 🎯 应用场景

UI-TARS-2具有广泛的应用前景，包括自动化测试、智能助手、软件开发辅助工具等。它可以应用于各种需要与图形用户界面交互的场景，例如自动化执行重复性任务、辅助用户完成复杂操作、以及自动化测试软件的功能和性能。该研究的实际价值在于提高工作效率、降低开发成本、并提升用户体验。未来，UI-TARS-2有望成为智能交互领域的重要技术支撑。

## 📄 摘要（原文）

> The development of autonomous agents for graphical user interfaces (GUIs) presents major challenges in artificial intelligence. While recent advances in native agent models have shown promise by unifying perception, reasoning, action, and memory through end-to-end learning, open problems remain in data scalability, multi-turn reinforcement learning (RL), the limitations of GUI-only operation, and environment stability. In this technical report, we present UI-TARS-2, a native GUI-centered agent model that addresses these challenges through a systematic training methodology: a data flywheel for scalable data generation, a stabilized multi-turn RL framework, a hybrid GUI environment that integrates file systems and terminals, and a unified sandbox platform for large-scale rollouts. Empirical evaluation demonstrates that UI-TARS-2 achieves significant improvements over its predecessor UI-TARS-1.5. On GUI benchmarks, it reaches 88.2 on Online-Mind2Web, 47.5 on OSWorld, 50.6 on WindowsAgentArena, and 73.3 on AndroidWorld, outperforming strong baselines such as Claude and OpenAI agents. In game environments, it attains a mean normalized score of 59.8 across a 15-game suite-roughly 60% of human-level performance-and remains competitive with frontier proprietary models (e.g., OpenAI o3) on LMGame-Bench. Additionally, the model can generalize to long-horizon information-seeking tasks and software engineering benchmarks, highlighting its robustness across diverse agent tasks. Detailed analyses of training dynamics further provide insights into achieving stability and efficiency in large-scale agent RL. These results underscore UI-TARS-2's potential to advance the state of GUI agents and exhibit strong generalization to real-world interactive scenarios.

