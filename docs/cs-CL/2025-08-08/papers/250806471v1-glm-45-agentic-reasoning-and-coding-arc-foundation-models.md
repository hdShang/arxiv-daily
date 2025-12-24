---
layout: default
title: "GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models"
---

# GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06471" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06471v1</a>
  <a href="https://arxiv.org/pdf/2508.06471.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06471v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06471v1', 'GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: GLM-4. 5 Team, :, Aohan Zeng, Xin Lv, Qinkai Zheng, Zhenyu Hou, Bin Chen, Chengxing Xie, Cunxiang Wang, Da Yin, Hao Zeng, Jiajie Zhang, Kedong Wang, Lucen Zhong, Mingdao Liu, Rui Lu, Shulin Cao, Xiaohan Zhang, Xuancheng Huang, Yao Wei, Yean Cheng, Yifan An, Yilin Niu, Yuanhao Wen, Yushi Bai, Zhengxiao Du, Zihan Wang, Zilin Zhu, Bohan Zhang, Bosi Wen, Bowen Wu, Bowen Xu, Can Huang, Casey Zhao, Changpeng Cai, Chao Yu, Chen Li, Chendi Ge, Chenghua Huang, Chenhui Zhang, Chenxi Xu, Chenzheng Zhu, Chuang Li, Congfeng Yin, Daoyan Lin, Dayong Yang, Dazhi Jiang, Ding Ai, Erle Zhu, Fei Wang, Gengzheng Pan, Guo Wang, Hailong Sun, Haitao Li, Haiyang Li, Haiyi Hu, Hanyu Zhang, Hao Peng, Hao Tai, Haoke Zhang, Haoran Wang, Haoyu Yang, He Liu, He Zhao, Hongwei Liu, Hongxi Yan, Huan Liu, Huilong Chen, Ji Li, Jiajing Zhao, Jiamin Ren, Jian Jiao, Jiani Zhao, Jianyang Yan, Jiaqi Wang, Jiayi Gui, Jiayue Zhao, Jie Liu, Jijie Li, Jing Li, Jing Lu, Jingsen Wang, Jingwei Yuan, Jingxuan Li, Jingzhao Du, Jinhua Du, Jinxin Liu, Junkai Zhi, Junli Gao, Ke Wang, Lekang Yang, Liang Xu, Lin Fan, Lindong Wu, Lintao Ding, Lu Wang, Man Zhang, Minghao Li, Minghuan Xu, Mingming Zhao, Mingshu Zhai, Pengfan Du, Qian Dong, Shangde Lei, Shangqing Tu, Shangtong Yang, Shaoyou Lu, Shijie Li, Shuang Li, Shuang-Li, Shuxun Yang, Sibo Yi, Tianshu Yu, Wei Tian, Weihan Wang, Wenbo Yu, Weng Lam Tam, Wenjie Liang, Wentao Liu, Xiao Wang, Xiaohan Jia, Xiaotao Gu, Xiaoying Ling, Xin Wang, Xing Fan, Xingru Pan, Xinyuan Zhang, Xinze Zhang, Xiuqing Fu, Xunkai Zhang, Yabo Xu, Yandong Wu, Yida Lu, Yidong Wang, Yilin Zhou, Yiming Pan, Ying Zhang, Yingli Wang, Yingru Li, Yinpei Su, Yipeng Geng, Yitong Zhu, Yongkun Yang, Yuhang Li, Yuhao Wu, Yujiang Li, Yunan Liu, Yunqing Wang, Yuntao Li, Yuxuan Zhang, Zezhen Liu, Zhen Yang, Zhengda Zhou, Zhongpei Qiao, Zhuoer Feng, Zhuorui Liu, Zichen Zhang, Zihan Wang, Zijun Yao, Zikang Wang, Ziqiang Liu, Ziwei Chai, Zixuan Li, Zuodong Zhao, Wenguang Chen, Jidong Zhai, Bin Xu, Minlie Huang, Hongning Wang, Juanzi Li, Yuxiao Dong, Jie Tang

**分类**: cs.CL

**发布日期**: 2025-08-08

**🔗 代码/项目**: [GITHUB](https://github.com/zai-org/GLM-4.5)

---

## 💡 一句话要点

**提出GLM-4.5以推动智能推理与编码任务的研究**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `大型语言模型` `智能推理` `编码任务` `强化学习` `多阶段训练` `参数效率`

## 📋 核心要点

1. 现有大型语言模型在推理和编码任务上存在性能不足的问题，尤其是在参数效率方面。
2. GLM-4.5通过混合专家架构和多阶段训练，结合强化学习，提升了模型的推理能力和响应效率。
3. 在多项基准测试中，GLM-4.5表现优异，尤其在智能基准测试中排名第二，显示出其强大的应用潜力。

## 📝 摘要（中文）

我们提出了GLM-4.5，这是一个开源的混合专家（MoE）大型语言模型，具有3550亿个总参数和320亿个激活参数，采用混合推理方法，支持思考和直接响应模式。通过对23万亿个标记的多阶段训练和专家模型迭代及强化学习的全面后训练，GLM-4.5在智能、推理和编码（ARC）任务上表现出色，在TAU-Bench上得分70.1%，在AIME 24上得分91.0%，在SWE-bench Verified上得分64.2%。GLM-4.5的参数数量远少于多个竞争对手，在所有评估模型中排名第三，在智能基准测试中排名第二。我们发布了GLM-4.5（3550亿参数）和紧凑版GLM-4.5-Air（1060亿参数），以推动推理和智能AI系统的研究。代码、模型及更多信息可在https://github.com/zai-org/GLM-4.5获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有大型语言模型在智能推理和编码任务中的性能不足，尤其是参数效率低的问题。现有模型往往需要大量参数才能实现较好的性能，限制了其应用范围。

**核心思路**：GLM-4.5采用混合专家（MoE）架构，结合多阶段训练和强化学习，旨在通过激活部分参数来提高模型的推理能力和响应速度，从而在保持较低参数量的同时实现高效性能。

**技术框架**：GLM-4.5的整体架构包括多个模块：首先是混合专家模块，通过选择性激活来优化计算资源；其次是多阶段训练流程，利用23万亿个标记进行预训练，最后通过专家模型迭代和强化学习进行后训练，以提升模型的智能和推理能力。

**关键创新**：GLM-4.5的主要创新在于其混合专家架构的设计，使得模型在参数数量较少的情况下，依然能够在多个智能推理任务中表现出色。这一设计与传统的全参数模型有本质区别，显著提高了参数利用率。

**关键设计**：在模型设计中，GLM-4.5采用了3550亿个总参数和320亿个激活参数的配置，优化了损失函数和网络结构，以适应混合专家的需求。此外，强化学习的引入进一步提升了模型在复杂任务中的表现。

## 📊 实验亮点

GLM-4.5在多个基准测试中取得了优异的成绩，特别是在TAU-Bench上得分70.1%，在AIME 24上得分91.0%，在SWE-bench Verified上得分64.2%。相比于其他大型模型，GLM-4.5以更少的参数数量实现了更高的性能，显示出其在智能推理任务中的竞争力。

## 🎯 应用场景

GLM-4.5在智能推理和编码任务中具有广泛的应用潜力，能够支持自然语言处理、代码生成、智能问答等领域。其高效的参数利用率和强大的推理能力使其在实际应用中具备显著的价值，未来可能推动更多智能AI系统的发展。

## 📄 摘要（原文）

> We present GLM-4.5, an open-source Mixture-of-Experts (MoE) large language model with 355B total parameters and 32B activated parameters, featuring a hybrid reasoning method that supports both thinking and direct response modes. Through multi-stage training on 23T tokens and comprehensive post-training with expert model iteration and reinforcement learning, GLM-4.5 achieves strong performance across agentic, reasoning, and coding (ARC) tasks, scoring 70.1% on TAU-Bench, 91.0% on AIME 24, and 64.2% on SWE-bench Verified. With much fewer parameters than several competitors, GLM-4.5 ranks 3rd overall among all evaluated models and 2nd on agentic benchmarks. We release both GLM-4.5 (355B parameters) and a compact version, GLM-4.5-Air (106B parameters), to advance research in reasoning and agentic AI systems. Code, models, and more information are available at https://github.com/zai-org/GLM-4.5.

