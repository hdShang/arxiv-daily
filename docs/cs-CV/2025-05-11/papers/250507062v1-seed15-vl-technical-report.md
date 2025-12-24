---
layout: default
title: Seed1.5-VL Technical Report
---

# Seed1.5-VL Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07062" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07062v1</a>
  <a href="https://arxiv.org/pdf/2505.07062.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07062v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07062v1', 'Seed1.5-VL Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dong Guo, Faming Wu, Feida Zhu, Fuxing Leng, Guang Shi, Haobin Chen, Haoqi Fan, Jian Wang, Jianyu Jiang, Jiawei Wang, Jingji Chen, Jingjia Huang, Kang Lei, Liping Yuan, Lishu Luo, Pengfei Liu, Qinghao Ye, Rui Qian, Shen Yan, Shixiong Zhao, Shuai Peng, Shuangye Li, Sihang Yuan, Sijin Wu, Tianheng Cheng, Weiwei Liu, Wenqian Wang, Xianhan Zeng, Xiao Liu, Xiaobo Qin, Xiaohan Ding, Xiaojun Xiao, Xiaoying Zhang, Xuanwei Zhang, Xuehan Xiong, Yanghua Peng, Yangrui Chen, Yanwei Li, Yanxu Hu, Yi Lin, Yiyuan Hu, Yiyuan Zhang, Youbin Wu, Yu Li, Yudong Liu, Yue Ling, Yujia Qin, Zanbo Wang, Zhiwu He, Aoxue Zhang, Bairen Yi, Bencheng Liao, Can Huang, Can Zhang, Chaorui Deng, Chaoyi Deng, Cheng Lin, Cheng Yuan, Chenggang Li, Chenhui Gou, Chenwei Lou, Chengzhi Wei, Chundian Liu, Chunyuan Li, Deyao Zhu, Donghong Zhong, Feng Li, Feng Zhang, Gang Wu, Guodong Li, Guohong Xiao, Haibin Lin, Haihua Yang, Haoming Wang, Heng Ji, Hongxiang Hao, Hui Shen, Huixia Li, Jiahao Li, Jialong Wu, Jianhua Zhu, Jianpeng Jiao, Jiashi Feng, Jiaze Chen, Jianhui Duan, Jihao Liu, Jin Zeng, Jingqun Tang, Jingyu Sun, Joya Chen, Jun Long, Junda Feng, Junfeng Zhan, Junjie Fang, Junting Lu, Kai Hua, Kai Liu, Kai Shen, Kaiyuan Zhang, Ke Shen, Ke Wang, Keyu Pan, Kun Zhang, Kunchang Li, Lanxin Li, Lei Li, Lei Shi, Li Han, Liang Xiang, Liangqiang Chen, Lin Chen, Lin Li, Lin Yan, Liying Chi, Longxiang Liu, Mengfei Du, Mingxuan Wang, Ningxin Pan, Peibin Chen, Pengfei Chen, Pengfei Wu, Qingqing Yuan, Qingyao Shuai, Qiuyan Tao, Renjie Zheng, Renrui Zhang, Ru Zhang, Rui Wang, Rui Yang, Rui Zhao, Shaoqiang Xu, Shihao Liang, Shipeng Yan, Shu Zhong, Shuaishuai Cao, Shuangzhi Wu, Shufan Liu, Shuhan Chang, Songhua Cai, Tenglong Ao, Tianhao Yang, Tingting Zhang, Wanjun Zhong, Wei Jia, Wei Weng, Weihao Yu, Wenhao Huang, Wenjia Zhu, Wenli Yang, Wenzhi Wang, Xiang Long, XiangRui Yin, Xiao Li, Xiaolei Zhu, Xiaoying Jia, Xijin Zhang, Xin Liu, Xinchen Zhang, Xinyu Yang, Xiongcai Luo, Xiuli Chen, Xuantong Zhong, Xuefeng Xiao, Xujing Li, Yan Wu, Yawei Wen, Yifan Du, Yihao Zhang, Yining Ye, Yonghui Wu, Yu Liu, Yu Yue, Yufeng Zhou, Yufeng Yuan, Yuhang Xu, Yuhong Yang, Yun Zhang, Yunhao Fang, Yuntao Li, Yurui Ren, Yuwen Xiong, Zehua Hong, Zehua Wang, Zewei Sun, Zeyu Wang, Zhao Cai, Zhaoyue Zha, Zhecheng An, Zhehui Zhao, Zhengzhuo Xu, Zhipeng Chen, Zhiyong Wu, Zhuofan Zheng, Zihao Wang, Zilong Huang, Ziyu Zhu, Zuquan Song

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-11

---

## 💡 一句话要点

**提出Seed1.5-VL以解决多模态理解与推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态理解` `视觉-语言模型` `混合专家` `推理能力` `图像描述` `视觉问答` `智能代理`

## 📋 核心要点

1. 现有多模态模型在理解和推理能力上存在不足，难以有效处理复杂的视觉和语言任务。
2. Seed1.5-VL结合了视觉编码器和混合专家大语言模型，旨在提升多模态理解和推理的性能。
3. 在实验中，Seed1.5-VL在60个公共基准中取得了38个最先进的结果，并在多项代理任务中超越了现有系统。

## 📝 摘要（中文）

我们提出了Seed1.5-VL，这是一个旨在推动通用多模态理解和推理的视觉-语言基础模型。Seed1.5-VL由一个532M参数的视觉编码器和一个具有20B活跃参数的混合专家（MoE）大语言模型组成。尽管其架构相对紧凑，但在多个公共VLM基准和内部评估套件上表现出色，在60个公共基准中有38个达到了最先进的性能。此外，在GUI控制和游戏等以代理为中心的任务中，Seed1.5-VL超越了包括OpenAI CUA和Claude 3.7在内的领先多模态系统。除了视觉和视频理解外，它还展现了强大的推理能力，使其在视觉难题等多模态推理挑战中尤为有效。我们希望这些能力能够推动更广泛的应用。

## 🔬 方法详解

**问题定义**：本论文旨在解决当前多模态模型在理解和推理能力上的不足，尤其是在复杂任务中的表现不佳。现有方法往往无法有效整合视觉和语言信息，导致推理能力受限。

**核心思路**：Seed1.5-VL通过结合一个532M参数的视觉编码器和一个20B参数的混合专家大语言模型，旨在提升多模态理解和推理的能力。这样的设计使得模型在保持相对紧凑的同时，能够处理复杂的多模态任务。

**技术框架**：Seed1.5-VL的整体架构包括视觉编码器和语言模型两大模块。视觉编码器负责提取图像特征，而语言模型则通过混合专家机制增强其推理能力。模型的训练过程分为多个阶段，以确保在不同任务上的适应性和性能。

**关键创新**：最重要的技术创新在于引入了混合专家机制，使得模型在处理多模态信息时能够动态选择最相关的专家进行推理。这一设计显著提升了模型的灵活性和性能。

**关键设计**：在模型设计中，采用了532M参数的视觉编码器和20B活跃参数的语言模型。损失函数的设计考虑了多模态信息的融合，确保了视觉和语言特征的有效整合。

## 📊 实验亮点

Seed1.5-VL在60个公共基准中取得了38个最先进的结果，表现优于OpenAI CUA和Claude 3.7等领先多模态系统。在代理任务中，其性能提升显著，展示了强大的多模态推理能力。

## 🎯 应用场景

Seed1.5-VL在多模态理解和推理领域具有广泛的应用潜力，能够用于图像描述、视觉问答、智能代理等任务。其强大的推理能力使其在复杂场景下的应用价值显著，未来可能推动更多智能系统的开发与应用。

## 📄 摘要（原文）

> We present Seed1.5-VL, a vision-language foundation model designed to advance general-purpose multimodal understanding and reasoning. Seed1.5-VL is composed with a 532M-parameter vision encoder and a Mixture-of-Experts (MoE) LLM of 20B active parameters. Despite its relatively compact architecture, it delivers strong performance across a wide spectrum of public VLM benchmarks and internal evaluation suites, achieving the state-of-the-art performance on 38 out of 60 public benchmarks. Moreover, in agent-centric tasks such as GUI control and gameplay, Seed1.5-VL outperforms leading multimodal systems, including OpenAI CUA and Claude 3.7. Beyond visual and video understanding, it also demonstrates strong reasoning abilities, making it particularly effective for multimodal reasoning challenges such as visual puzzles. We believe these capabilities will empower broader applications across diverse tasks. In this report, we mainly provide a comprehensive review of our experiences in building Seed1.5-VL across model design, data construction, and training at various stages, hoping that this report can inspire further research. Seed1.5-VL is now accessible at https://www.volcengine.com/ (Volcano Engine Model ID: doubao-1-5-thinking-vision-pro-250428)

